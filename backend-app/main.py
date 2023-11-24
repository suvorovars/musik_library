from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy.orm import class_mapper

from db import db_session
from db.disks import Disks
from db.tracks import Tracks
from db.performers import Performers
from db.genres import Genres
from db.strings import Strings
import constants

app = Flask(__name__)
CORS(app)  # Это добавляет CORS заголовки ко всем маршрутам

db_session.global_init(
    f'postgresql+pg8000://{constants.db_admin}:{constants.db_password}@localhost:5432/{constants.db_name}')

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
    session = db_session.create_session()
    if form['genre_title'] is not None:
        new_genre = Genres(genre_title=form['genre_title'])
        session.add(new_genre)
        return jsonify({'success': True})
    return jsonify({'success': False})


@app.route('/api/add/performers', methods=['POST'])
def add_performers():
    form = request.get_json(force=True)
    session = db_session.create_session()
    if form['performer_name'] is not None:
        new_performer = Performers(performer_name=form['performer_name'])
        session.add(new_performer)
        return jsonify({'success': True})
    return jsonify({'success': False})


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
