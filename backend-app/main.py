from flask import Flask, jsonify, request
from db import db_session
from db.disks import Disks
from db.tracks import Tracks
from db.performers import Performers
from db.genres import Genres
from db.strings import Strings
import constants

app = Flask(__name__)

db_session.global_init(
    f'postgresql+pg8000://{constants.db_admin}:{constants.db_password}@localhost:5432/{constants.db_name}')


@app.route('/api/test')
def test():
    session = db_session.create_session()
    response = session.query(Strings).all()
    return response


@app.route('/api/add/genres', methods=['POST', 'GET'])
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


app.run()
