from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from db import session
from db.tables.disks import Disks
from db.tables.tracks import Tracks
from db.tables.performers import Performers
from db.tables.genres import Genres
from db.tables.strings import Strings

import parser.yandex_music_parser as parser

import os

app = Flask(__name__)
CORS(app)  # Это добавляет CORS заголовки ко всем маршрутам

@app.route('/api/')

@app.route('/api/gather/performers', methods=['POST'])
def gather_performers():
    nickname = request.form.get('nickname')
    conn = session.create_session()
    if session.get_performers(conn, nickname) != []:
        return {"success": False, "result": "You cannot add this performer! Probably he already exists."}
    client = parser.get_client()
    performer_info = parser.search_artists(client, nickname)
    session.add_performer(conn, performer_info[0]['artist_name'])
    for track_info in performer_info:
        track_title = track_info['track_title']
        genre_name = track_info['genre']

        if session.get_genres(conn, genre_name=genre_name) == []:
            session.add_genre(conn, genre_name)
        if session.get_tracks(conn, track_title) == []:
            session.add_track(conn, track_title)

    return {"success": True}

@app.route('/api/create/string', methods=['POST'])
def create_string():
    pass

@app.route('/api/create/disk', methods=['POST'])
def create_disk():
    pass

@app.route('/api/get/strings', methods=['GET'])
def get_strings():
    conn = session.create_session()

    string_id = request.args.get('string_id')
    limit = request.args.get('limit')

    if not(string_id):
        return {'status': False}
    
    string_id = int(string_id)
    limit = 5 if not(limit) else int(limit)
    strings = session.get_strings(conn, string_id=string_id, limit=limit)

    print(strings)

    return {'status': True}

@app.route('/', methods=['GET'])
def main():
    return "hello, world!"


app.run()

