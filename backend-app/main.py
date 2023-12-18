from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy.orm import class_mapper

from db import db_session, instructions
from db.tables.disks import Disks
from db.tables.tracks import Tracks
from db.tables.performers import Performers
from db.tables.genres import Genres
from db.tables.strings import Strings

import db.db_config as config

from parser import yandex_music_parser as parser


app = Flask(__name__)
CORS(app)  # Это добавляет CORS заголовки ко всем маршрутам

db_session.global_init(
    f'postgresql+pg8000://{config.db_admin}:{config.db_password}@localhost:5432/{config.db_name}'
)


def custom_json(obj):
    if hasattr(obj, '__table__'):
        return {c.key: getattr(obj, c.key) for c in class_mapper(obj.__class__).columns}
    raise TypeError("Object of type '{}' is not JSON serializable".format(type(obj)))


@app.route('/api/gather/performers', methods=['POST'])
def gather_performers():
    form = request.get_json(force=True)
    if form.get('nickname') is None:
        return jsonify({'success': False})
    nickname = form.get('nickname').upper()
    print(nickname)
    conn = db_session.create_connection()
    if instructions.get_performers(conn, nickname) != []:
        return {"success": False, "result": "You cannot add this performer! Probably he already exists."}
    client = parser.get_client()
    performer_info = parser.search_artists(client, nickname)
    instructions.add_performer(conn, performer_info[0]['artist_name'])

    for track_info in performer_info:
        track_title = track_info['track_title']
        genre_name = track_info['genre']

        if instructions.get_genres(conn, genre_title=genre_name) == []:
            instructions.add_genre(conn, genre_name)
        if instructions.get_tracks(conn, track_title) == []:
            instructions.add_track(conn, track_title)

    return {"success": True}


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
    print(form.get('disk_title'))
    print(form.get('disk_year'))
    if (form.get('disk_title') and form.get('disk_year')) is None:
        return jsonify({'success': False, 'error': "wrong data request!"})
    if (len(form.get('disk_title')) != len(form.get('disk_year'))):
        return jsonify({'success': False, 'error': 'Different length of your data request!'})

    connection = db_session.create_connection()

    for disk_title, disk_year in zip(form.get('disk_title'), form.get('disk_year')):
        instructions.add_disk(connection, disk_title, disk_year)
    return jsonify({'success': True})


@app.route('/api/add/strings', methods=['POST'])
def add_strings():
    form = request.get_json(force=True)
    if (form.get('disk_fk') and form.get('track_fk') and form.get('genre_fk') and form.get('duration') and form.get(
            'performer_fk')) is None:
        return jsonify({'success': False, 'type': 'wrong data request!'})

    if (len(form.get('disk_fk')) != len(form.get('track_fk')) != len(form.get('genre_fk')) != len(
            form.get('duration')) != len(form.get('performer_fk'))):
        return jsonify({'success': False, 'type': 'Different length of your data request!'})

    connection = db_session.create_connection()
    for disk_fk, track_fk, genre_fk, performer_fk, duration in zip(
                form.get('disk_fk'),
                form.get('track_fk'),
                form.get('genre_fk'),
                form.get('performer_fk'),
                form.get('duration')):
        string_number = instructions.get_string_number(connection, disk_fk)
        string_number = string_number[0][0] if string_number else 0
        instructions.add_string(connection,
                                disk_fk=disk_fk,
                                track_fk=track_fk,
                                genre_fk=genre_fk,
                                performer_fk=performer_fk,
                                duration=duration,
                                string_num=string_number + 1)

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

@app.route('/api/get/strs', methods=['GET'])
def get_strs():
    disk_id = request.args.get('disk_fk')
    response_json = []
    data_frame = {
        'id': None,
        'track_title': None,
        'performer_name': None,
        'genre_title' : None,
        'duration': None,
    }
    if disk_id is None:
        return jsonify({'success': False})
    disk_id = int(disk_id)
    session = db_session.create_session()
    response = session.query(
            Strings.string_number,
            Tracks.track_title,
            Performers.performer_name,
            Genres.genre_title,
            Strings.duration,
            Strings.disk_fk
        ).join(Tracks, Tracks.track_id == Strings.track_fk
               ).join(Performers, Performers.performer_id == Strings.performer_fk
                      ).join(Genres, Genres.genre_id == Strings.genre_fk).filter(Strings.disk_fk == disk_id).all()
    for string_info in response:
        data_frame = {
            'id': string_info[0],
            'track_title': string_info[1],
            'performer_name': string_info[2],
            'genre_title': string_info[3],
            'duration': string_info[4]
        }
        response_json.append(data_frame)

    return jsonify(response_json)

@app.route('/api/get/strings', methods=['GET'])
def get_strings():
    response_json = []
    session = db_session.create_session()
    lst_disks = session.query(Disks.disk_id, Disks.disk_title, Disks.year).all()
    for i in lst_disks:

        data_frame = {
            'id': i[0],
            'disk_title': i[1],
            'year': i[2],
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
    return jsonify(response_json)

@app.route('/api/get/string_values', methods=['GET'])
def get_string_values():

    disk_fk = request.args.get('disk_fk')
    genre_fk = request.args.get('genre_fk')
    track_fk = request.args.get('track_fk')
    performer_fk = request.args.get('performer_fk')
    string_num = request.args.get('string_number')

    response_json = []

    connection = db_session.create_connection()
    strings = instructions.get_strings(connection, disk_fk = disk_fk, genre_fk = genre_fk, track_fk = track_fk, performer_fk = performer_fk, string_number = string_num)
    print(strings)
    for string_info in strings:

        data_frame = {
            'id': string_info[0],
            'disk_fk': string_info[1],
            'string_number': string_info[2],
            'track_fk': string_info[3],
            'performer_fk': string_info[4],
            'genre_fk': string_info[5],
            'duration': string_info[6]
            }
    
        response_json.append(data_frame)
    return jsonify(response_json)

@app.route('/api/get/performers', methods=['GET'])
def get_performers():
    response_json = []
    performer_name = request.args.get('performer_name')
    connection = db_session.create_connection()
    performers = instructions.get_performers(connection, performer_name)
    for performer_info in performers:
        data_frame = {
            'performer_id': performer_info[0],
            'performer_name': performer_info[1]
        }

        response_json.append(data_frame)

    return jsonify(response_json)


@app.route('/api/get/tracks', methods=['GET'])
def get_tracks():
    response_json = []
    connection = db_session.create_connection()
    track_title = request.args.get('track_title') 
    tracks = instructions.get_tracks(connection, track_title)
    for track_info in tracks:
        data_frame = {
            'track_id': track_info[0],
            'track_title': track_info[1]
        }

        response_json.append(data_frame)

    return jsonify(response_json)


@app.route('/api/get/genres', methods=['GET'])
def get_genres():
    response_json = []
    connection = db_session.create_connection()
    genre_title = request.args.get('genre_title')
    genres = instructions.get_genres(connection, genre_title)
    for genre_info in genres:
        data_frame = {
            'genre_id': genre_info[0],
            'genre_title': genre_info[1]
        }

        response_json.append(data_frame)

    return jsonify(response_json)


@app.route('/api/get/disks', methods=['GET'])
def get_disks():
    response_json = []
    connection = db_session.create_connection()
    disks = instructions.get_disks(connection)
    for disk_info in disks:
        data_frame = {
            'disk_id': disk_info[0],
            'disk_title': disk_info[1],
            'year': disk_info[2],
        }

        response_json.append(data_frame)

    return jsonify(response_json)
@app.route('/api/edit/disks', methods=['POST'])
def edit_disks():
    form = request.get_json(force=True)
    print(form.get('old_disk_id'))
    connection = db_session.create_connection()

    instructions.update_disks(connection,
                              form.get('old_disk_id'),
                              form.get('old_disk_title'),
                              form.get('old_year'),
                              form.get('new_disk_id'),
                              form.get('new_disk_title'),
                              form.get('new_year'))
    
    return jsonify({'success': True})

@app.route('/api/edit/strings', methods=['POST'])
def edit_strings():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.update_strings(connection,
                              form.get('old_id'),
                              form.get('old_string_number'),
                              form.get('old_disk_fk'),
                              form.get('old_track_fk'),
                              form.get('old_genre_fk'),
                              form.get('old_performer_fk'),
                              form.get('old_duration'),
                              form.get('new_id'),
                              form.get('new_string_number'),
                              form.get('new_disk_fk'),
                              form.get('new_track_fk'),
                              form.get('new_genre_fk'),
                              form.get('new_performer_fk'),
                              form.get('new_duration'),
    )
    
    return jsonify({'success': True})

@app.route('/api/edit/tracks', methods=['POST'])
def edit_tracks():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.update_tracks(connection,
                               form.get('old_track_id'),
                               form.get('old_track_title'),
                               form.get('new_track_id'),
                               form.get('new_track_title')
    )
    
    return jsonify({'success': True})

@app.route('/api/edit/performers', methods=['POST'])
def edit_performers():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.update_performers(connection,
                               form.get('old_performer_id'),
                               form.get('old_performer_name'),
                               form.get('new_performer_id'),
                               form.get('new_performer_name')
    )
    
    return jsonify({'success': True})

@app.route('/api/edit/genres', methods=['POST'])
def edit_genres():
    form = request.get_json(force=True)
    connection = db_session.create_connection()
    instructions.update_genres(connection,
                               form.get('old_genre_id'),
                               form.get('old_genre_title'),
                               form.get('new_genre_id'),
                               form.get('new_genre_title')
    )
    
    return jsonify({'success': True})

@app.route('/api/delete/disks', methods=['POST'])
def delete_disks():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.delete_disks(connection,
        form.get('disk_id'),
        form.get('disk_title'),
        form.get('year'))
    return jsonify({'success': True})


@app.route('/api/delete/strings', methods=['POST'])
def delete_strings():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.delete_strings(
        connection,
        form.get('id'),
        form.get('string_number'),
        form.get('disk_fk'),
        form.get('performer_fk'),
        form.get('track_fk'),
        form.get('genre_fk'),
        form.get('duration'),
    )
    
    return jsonify({'success': True})

@app.route('/api/delete/tracks', methods=['POST'])
def delete_tracks():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.delete_tracks(connection,
        form.get('track_id'),
        form.get('track_title')
        )
    return jsonify({'success': True})

@app.route('/api/delete/genres', methods=['POST'])
def delete_genres():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.delete_genres(connection,
        form.get('genre_id'),
        form.get('genre_title')
        )
    
    return jsonify({'success': True})

@app.route('/api/delete/performers', methods=['POST'])
def delete_performers():
    form = request.get_json(force=True)
    connection = db_session.create_connection()

    instructions.delete_performers(connection,
        form.get('performer_id'),
        form.get('performer_name')
        )
    
    return jsonify({'success': True})

@app.route('/api/get/count', methods=['GET'])
def get_counts():
    connection = db_session.create_connection()

    track_title = request.args.get('track_title')
    genre_title = request.args.get('genre_title')
    performer_name = request.args.get('performer_name')

    track_fk = None
    genre_fk = None
    performer_fk = None

    if track_title:
        track_fk = instructions.get_tracks(connection, track_title=track_title)
        if track_fk != []:
            track_fk = track_fk[0][0]
        else:
            track_fk = None
    if genre_title:
        genre_fk = instructions.get_genres(connection, genre_title=genre_title)
        if genre_fk != []:
            genre_fk = genre_fk[0][0]
        else:
            genre_fk = None
    if performer_name:
        performer_fk = instructions.get_performers(connection, nickname=performer_name)
        if performer_fk != []:
            performer_fk = performer_fk[0][0]
        else:
            performer_fk = None

    print(instructions.get_count(connection, track_fk=track_fk, genre_fk=genre_fk, performer_fk=performer_fk).fetchall())
    return jsonify({'success': True})

# app.run(port=8000)
