import sqlalchemy

from .tables.disks import Disks
from .tables.genres import Genres
from .tables.performers import Performers
from .tables.strings import Strings
from .tables.tracks import Tracks


def add_genre(connection, genre_title: str):
    query = sqlalchemy.insert(Genres).values({'genre_title': genre_title})
    connection.execute(query)
    connection.commit()


def add_performer(connection, performer_name: str):
    query = sqlalchemy.insert(Performers).values({'performer_name': performer_name})
    connection.execute(query)
    connection.commit()


def add_disk(connection, disk_name: str, disk_date: int):
    query = sqlalchemy.insert(Disks).values({'disk_title': disk_name, 'year': disk_date})
    connection.execute(query)
    connection.commit()


def add_track(connection, track_title: str):
    query = sqlalchemy.insert(Tracks).values({'track_title': track_title})
    connection.execute(query)
    connection.commit()


def add_string(connection, disk_fk: int, performer_fk: int, track_fk: int, genre_fk: int, string_num: int, duration: int):
    print(disk_fk, performer_fk, track_fk, genre_fk, string_num, duration)
    query = sqlalchemy.insert(Strings).values(
        {'disk_fk': disk_fk, 'performer_fk': performer_fk, 'track_fk': track_fk, 'genre_fk': genre_fk,
         'string_number': string_num, 'duration': duration})
    connection.execute(query)
    connection.commit()


def get_genres(connection, genre_title=None):
    if genre_title:
        query = sqlalchemy.select(Genres).where(Genres.genre_title == genre_title)
    else:
        query = sqlalchemy.select(Genres)

    return connection.execute(query).fetchall()


def get_performers(connection, nickname=None):
    if nickname:
        query = sqlalchemy.select(Performers).where(Performers.performer_name == nickname)
    else:
        query = sqlalchemy.select(Performers)

    return connection.execute(query).fetchall()


def get_tracks(connection, track_title=None):
    if track_title:
        query = sqlalchemy.select(Tracks).where(Tracks.track_title == track_title)
    else:
        query = sqlalchemy.select(Tracks)

    return connection.execute(query).fetchall()


def get_disks(connection, disk_id=None, disk_title=None):
    query = sqlalchemy.select(Disks)
    if disk_id:
        query = query.where(Disks.disk_id == disk_id)
    if disk_title:
        query = query.where(Disks.disk_title == disk_title)

    return connection.execute(query).fetchall()


def get_strings(connection, string_id=None, limit=5):
    if string_id:
        query = sqlalchemy.select(Strings).where(Strings.id >= string_id).limit(limit)
    else:
        query = sqlalchemy.select(Strings).limit(5)
    return connection.execute(query).fetchall()


def get_string_number(connection, disk_fk: int):
    query = sqlalchemy.select(Strings.string_number).where(Strings.disk_fk == disk_fk).order_by(Strings.string_number.desc()).limit(1)
    return connection.execute(query).fetchall()


def update_disks(connection, old_disk_id=None, old_disk_title=None, old_year=None, new_disk_id=None, new_disk_title=None, new_year=None):
    query = sqlalchemy.update(Disks)
    if old_disk_id:
        query = query.where(Disks.disk_id == int(old_disk_id))
    if old_disk_title:
        query = query.where(Disks.disk_title == old_disk_title)
    if old_year:
        query = query.where(Disks.year == old_year)
    
    if new_disk_id:
        query = query.values(disk_id=new_disk_id)
    if new_disk_title:
        query = query.values(disk_title=new_disk_title)
    if new_year:
        query = query.values(year=new_year)
    
    connection.execute(query)
    connection.commit()

def update_tracks(connection, old_track_id=None, old_track_title=None, new_track_id=None, new_track_title=None):
    query = sqlalchemy.update(Tracks)
    if old_track_id:
        query = query.where(Tracks.track_id == old_track_id)
    if old_track_title:
        query = query.where(Tracks.track_title == old_track_title)
    
    if new_track_id:
        query = query.values(track_id=new_track_id)
    if new_track_title:
        query = query.values(track_title=new_track_title)

    connection.execute(query)
    connection.commit()

def update_performers(connection, old_performer_id=None, old_performer_name=None, new_performer_id=None, new_performer_name=None):
    query = sqlalchemy.update(Performers)
    if old_performer_id:
        query = query.where(Performers.performer_id == old_performer_id)
    if old_performer_name:
        query = query.where(Performers.performer_name == old_performer_name)
    
    if new_performer_id:
        query = query.values(performer_id=new_performer_id)
    if new_performer_name:
        query = query.values(performer_name=new_performer_name)

    print(old_performer_name, new_performer_name)

    connection.execute(query)
    connection.commit()

def update_genres(connection, old_genre_id=None, old_genre_title=None, new_genre_id=None, new_genre_title=None):
    query = sqlalchemy.update(Genres)
    if old_genre_id:
        query = query.where(Genres.genre_id == old_genre_id)
    if old_genre_title:
        query = query.where(Genres.genre_title == old_genre_title)
    
    if new_genre_id:
        query = query.values(genre_id=new_genre_id)
    if new_genre_title:
        query = query.values(genre_title=new_genre_title)

    connection.execute(query)
    connection.commit()

def update_strings(connection,
                   old_id=None, 
                   old_string_number=None, 
                   old_disk_fk=None, 
                   old_track_fk=None, 
                   old_genre_fk=None, 
                   old_performer_fk=None, 
                   old_duration=None, 
                   new_id=None, 
                   new_string_number=None, 
                   new_disk_fk=None, 
                   new_track_fk=None, 
                   new_genre_fk=None,
                   new_performer_fk=None, 
                   new_duration=None):
    query = sqlalchemy.update(Strings)
    if old_id:
        query = query.where(Strings.id == old_id)
    if old_string_number:
        query = query.where(Strings.string_number == old_string_number)
    if old_disk_fk:
        query = query.where(Strings.disk_fk == old_disk_fk)
    if old_track_fk:
        query = query.where(Strings.track_fk == old_track_fk)
    if old_performer_fk:
        query = query.where(Strings.performer_fk == old_performer_fk)
    if old_genre_fk:
        query = query.where(Strings.genre_fk == old_genre_fk)
    if old_duration:
        query = query.where(Strings.duration == old_duration)
    
    if new_id:
        query = query.values(disk_id=new_id)
    if new_string_number:
        query = query.values(string_number=new_string_number)
    if new_disk_fk:
        query = query.values(disk_fk=new_disk_fk)
    if new_track_fk:
        query = query.values(track_fk=new_disk_fk)
    if new_genre_fk:
        query = query.values(genre_fk=new_genre_fk)
    if new_performer_fk:
        query = query.values(performer_fk=new_performer_fk)
    if new_duration:
        query = query.values(duration=new_duration)

    connection.execute(query)
    connection.commit()

def delete_strings(connection, 
                   id=None, 
                   string_number=None, 
                   disk_fk=None,
                   performer_fk=None,
                   track_fk=None,
                   genre_fk=None,
                   duration=None):
    query = sqlalchemy.delete(Strings)
    if id:
        query = query.where(Strings.id == id)
    if string_number:
        query = query.where(Strings.string_number == string_number)
    if disk_fk:
        query = query.where(Strings.disk_fk == disk_fk)
    if track_fk:
        query = query.where(Strings.track_fk == track_fk)
    if performer_fk:
        query = query.where(Strings.performer_fk == performer_fk)
    if genre_fk:
        query = query.where(Strings.genre_fk == genre_fk)
    if duration:
        query = query.where(Strings.duration == duration)

    connection.execute(query)
    connection.commit()

def delete_disks(connection, disk_id=None, disk_title=None, year=None):
    query = sqlalchemy.delete(Disks)
    if disk_id:
        query = query.where(Disks.disk_id == disk_id)
    if disk_title:
        query = query.where(Disks.disk_title == disk_title)
    if year:
        query = query.where(Disks.year == year)
    
    connection.execute(query)
    connection.commit()

def delete_tracks(connection, track_id=None, track_title=None):
    query = sqlalchemy.delete(Tracks)

    if track_id:
        query = query.where(Tracks.track_id == track_id)
    if track_title:
        query = query.where(Tracks.track_title == track_title)
    
    connection.execute(query)
    connection.commit()

def delete_performers(connection, performer_id=None, performer_name=None):
    query = sqlalchemy.delete(Performers)

    if performer_id:
        query = query.where(Performers.performer_id == performer_id)
    if performer_name:
        query = query.where(Performers.performer_name == performer_name)
    
    connection.execute(query)
    connection.commit()

def delete_genres(connection, genres_id=None, genre_title=None):
    query = sqlalchemy.delete(Genres)

    if genres_id:
        query = query.where(Genres.genre_id == genres_id)
    if genre_title:
        query = query.where(Genres.genre_title == genre_title)
    
    connection.execute(query)
    connection.commit()