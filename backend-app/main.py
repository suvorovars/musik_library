from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy.orm import class_mapper

from db import db_session, instructions
from db.tables.disks import Disks
from db.tables.tracks import Tracks
from db.tables.performers import Performers
from db.tables.genres import Genres
from db.tables.strings import Strings
import config

from parser import yandex_music_parser as parser

app = Flask(__name__)
CORS(app)  # Это добавляет CORS заголовки ко всем маршрутам

db_session.global_init(
    f'postgresql+pg8000://{config.db_admin}:{config.db_password}@localhost:5432/{config.db_name}')

@app.route('/api/gather/performers', methods=['POST'])
def gather_performers():
    nickname = request.form.get('nickname')
    conn = db_session.create_connection()
    if instructions.get_performers(conn, nickname) != []:
        return {"success": False, "result": "You cannot add this performer! Probably he already exists."}
    client = parser.get_client()
    performer_info = parser.search_artists(client, nickname)
    instructions.add_performer(conn, performer_info[0]['artist_name'])
    for track_info in performer_info:
        track_title = track_info['track_title']
        genre_name = track_info['genre']

        if instructions.get_genres(conn, genre_name=genre_name) == []:
            instructions.add_genre(conn, genre_name)
        if instructions.get_tracks(conn, track_title) == []:
            instructions.add_track(conn, track_title)

    return {"success": True}

def custom_json(obj):
    if hasattr(obj, '__table__'):
        return {c.key: getattr(obj, c.key) for c in class_mapper(obj.__class__).columns}
    raise TypeError("Object of type '{}' is not JSON serializable".format(type(obj)))



@app.route('/api/test')
def test():
    response_json = []
    session = db_session.create_session()
    lst_disks = session.query(Disks.disk_id, Disks.disk_title, Disks.year).all()
    for i in lst_disks:
        data_frame = {
                'id': i[0],
                'disk': i[1],
                'strings': []
            }
        response = session.query(
            Strings.string_number,
            Tracks.track_title,
            Performers.performer_name,
            Genres.genre_title,
            Strings.duration,
            Strings.disk_fk
        ).join(Tracks, Tracks.track_id == Strings.track_fk
               ).join(Performers, Performers.performer_id == Strings.performer_fk
                      ).join(Genres, Genres.genre_id == Strings.genre_fk).filter(Strings.disk_fk == i[0]).all()
        for j in response:
            if j:
                data_frame['strings'].append({
                    'number': j[0],
                    'track_title': j[1],
                    'performer_name': j[2],
                    'genre_title': j[3],
                    'duration': j[4]
                })
        response_json.append(data_frame)
    print(response_json)
    return jsonify(response_json)


@app.route('/api/add/genres', methods=['POST'])
def add_genres():
    form = request.get_json(force=True)
    if form.get('genre') is None:
        return jsonify({'success': False})

    connection = db_session.create_connection()

    for genre in form.get('genre'):
        instructions.add_genre(connection, genre)
    return jsonify({'success': True})

@app.route('/api/add/tracks', methods=['POST'])
def add_tracks():
    form = request.get_json(force=True)
    if form.get('track') is None:
        return jsonify({'success': False})

    connection = db_session.create_connection()

    for track in form.get('track'):
        instructions.add_track(connection, track)
    return jsonify({'success': True})

@app.route('/api/add/disks', methods=['POST'])
def add_disks():
    form = request.get_json(force=True)
    if (form.get('disk_title') and form.get('disk_year')) is None:
        return jsonify({'success': False, 'error': 'Переданы не все данные!'})
    if (len(form.get('disk_title')) != len(form.get('disk_year'))):
        return jsonify({'success': False, 'error': 'Длина данных не совпадает'})

    connection = db_session.create_connection()

    for disk_title, disk_year in zip(form.get('disk'), form.get('disk_year')):
        instructions.add_disk(connection, disk_title, disk_year)
    return jsonify({'success': True})

@app.route('/api/add/strings', methods=['POST'])
def add_strings():
    form = request.get_json(force=True)
    if (form.get('disk_fk') and form.get('track_fk') and form.get('genre_fk') and form.get('duration') and form.get('performer_fk')) is None:
        return jsonify({'success': False, 'type': 'Переданы не все данные'})

    if (len(form.get('disk_fk')) != len(form.get('track_fk')) != len(form.get('genre_fk')) != len(form.get('duration')) != len(form.get('performer_fk'))):
        return jsonify({'success': False, 'type': 'Данные не совпадают по длине'})

    #TODO: высчитывать номер строки самостоятельно

    connection = db_session.create_connection()
    for disk_fk, track_fk, genre_fk, performer_fk, duration in zip(
                form.get('disk_fk'),
                form.get('track_fk'),
                form.get('genre_fk'),
                form.get('performer_fk'),
                form.get('duration')):
        string_number = instructions.get_string_number(connection, disk_fk)[0][0]
        instructions.add_string(connection,
                                disk_fk=disk_fk,
                                track_fk=track_fk,
                                genre_fk=genre_fk,
                                performer_fk=performer_fk,
                                duration=duration,
                                string_num=string_number+1)

    return jsonify({'success': True})

@app.route('/api/add/performers', methods=['POST'])
def add_performers():
    form = request.get_json(force=True)
    if form.get('performer') is None:
        return jsonify({'success': False})

    connection = db_session.create_connection()

    for performer in form.get('performer'):
        instructions.add_performer(connection, performer)
    return jsonify({'success': True})


@app.route('/api/get/strings', methods=['GET'])
def get_strings():
    response_json = []
    session = db_session.create_session()
    lst_disks = session.query(Disks.disk_id, Disks.disk_title, Disks.year).all()
    for i in lst_disks:

        data_frame = {
            'id': i[0],
            'disk': i[1],
            'strings': []
        }
        response = session.query(
            Strings.string_number,
            Tracks.track_title,
            Performers.performer_name,
            Genres.genre_title,
            Strings.duration,
            Strings.disk_fk
        ).join(Tracks, Tracks.track_id == Strings.track_fk
               ).join(Performers, Performers.performer_id == Strings.performer_fk
                      ).join(Genres, Genres.genre_id == Strings.genre_fk).filter(Strings.disk_fk == i[0]).all()
        for j in response:
            if j:
                data_frame['strings'].append({
                    'number': j[0],
                    'track_title': j[1],
                    'performer_name': j[2],
                    'genre_title': j[3],
                    'duration': j[4]
                })
        response_json.append(data_frame)
    print(response_json)
    return jsonify(response_json)


app.run(port=8000)
