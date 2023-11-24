import sqlalchemy

from .tables.disks import Disks
from .tables.genres import Genres
from .tables.performers import Performers
from .tables.strings import Strings
from .tables.tracks import Tracks


def add_genre(connection, genre_name: str):
    query = sqlalchemy.insert(Genres).values({'genre_name': genre_name})
    connection.execute(query)
    connection.commit()


def add_performer(connection, performer_name: str):
    query = sqlalchemy.insert(Performers).values({'performer_name': performer_name})
    connection.execute(query)
    connection.commit()


def add_disk(connection, disk_name: str, disk_date: int):
    query = sqlalchemy.insert(Disks).values({'disk_name': disk_name, 'disk_date': disk_date})
    connection.execute(query)
    connection.commit()


def add_track(connection, track_title: str):
    query = sqlalchemy.insert(Tracks).values({'track_title': track_title})
    connection.execute(query)
    connection.commit()


def add_string(connection, disk_fk: int, performer_fk: int, track_fk: int, genre_fk: int, string_num: int, duration: int):
    query = sqlalchemy.insert(Strings).values(
        {'disk_fk': disk_fk, 'performer_fk': performer_fk, 'track_fk': track_fk, 'genre_fk': genre_fk,
         'string_number': string_num, 'duration': duration})
    connection.execute(query)
    connection.commit()


def get_genres(connection, genre_name=None):
    if genre_name:
        query = sqlalchemy.select(Genres).where(Genres.genre_name == genre_name)
    else:
        query = sqlalchemy.select(Genres)

    return connection.execute(query).fetchall()


def get_performers(connection, nickname=None):
    if nickname:
        query = sqlalchemy.select(Performers).where(Performers.performer_nickname == nickname)
    else:
        query = sqlalchemy.select(Performers)

    return connection.execute(query).fetchall()


def get_tracks(connection, track_title=None):
    if track_title:
        query = sqlalchemy.select(Tracks).where(Tracks.track_title == track_title)
    else:
        query = sqlalchemy.select(Tracks)

    return connection.execute(query).fetchall()


def get_disks(connection, disk_id=None):
    if disk_id:
        query = sqlalchemy.select(Disks).where(Disks.disk_id == disk_id)
    else:
        query = sqlalchemy.select(Disks)

    return connection.execute(query).fetchall()


def get_strings(connection, string_id=None, limit=5):
    if string_id:
        query = sqlalchemy.select(Strings).where(Strings.string_id >= string_id).limit(limit)
    else:
        query = sqlalchemy.select(Strings).limit(5)
    return connection.execute(query).fetchall()

def get_string_number(connection, disk_fk: int):
    query = sqlalchemy.select(Strings.string_number).where(Strings.disk_fk == disk_fk).order_by(Strings.string_number.desc()).limit(1)
    return connection.execute(query).fetchall()