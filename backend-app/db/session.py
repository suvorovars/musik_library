from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from db.tables.db import DeclarativeBase
from db.tables.disks import Disks
from db.tables.genres import Genres
from db.tables.performers import Performers
from db.tables.tracks import Tracks
from db.tables.strings import Strings

from sqlalchemy import select, delete

from sqlalchemy.orm import sessionmaker

import sqlalchemy
import db.db_config as db_config

def create_session() -> sessionmaker:
    engine = create_engine(f"postgresql+pg8000://{db_config.user}:{db_config.password}@{db_config.host}:5432/{db_config.db_name}")
    DeclarativeBase.metadata.create_all(engine)

    connection = engine.connect()
    return connection

def add_genre(session, genre_name: str):
    query = sqlalchemy.insert(Genres).values({'genre_name':genre_name})
    session.execute(query)
    session.commit()

def add_performer(session: sessionmaker, performer_name: str):
    query = sqlalchemy.insert(Performers).values({'performer_name':performer_name})
    session.execute(query)
    session.commit()

def add_disk(session: sessionmaker, disk_name: str, disk_date: int):
    query = sqlalchemy.insert(Disks).values({'disk_name':disk_name, 'disk_date': disk_date})
    session.execute(query)
    session.commit()

def add_track(session: sessionmaker, track_title: str):
    query = sqlalchemy.insert(Tracks).values({'track_title':track_title})
    session.execute(query)
    session.commit()

def add_string(session: sessionmaker, disk_fk: int, performer_fk: int, track_fk: int, genre_fk: int, string_num: int):
    query = sqlalchemy.insert(Strings).values({'disk_fk':disk_fk, 'performer_fk': performer_fk, 'track_fk': track_fk, 'genre_fk':genre_fk, 'string_num': string_num})
    session.execute(query)
    session.commit()

def get_genres(session: sessionmaker, genre_name=None):
    if genre_name:
        query = select(Genres).where(Genres.genre_name == genre_name)
    else:
        query = select(Genres)
    
    return session.execute(query).fetchall()

def get_performers(session: sessionmaker, nickname=None):
    if nickname:
        query = select(Performers).where(Performers.performer_nickname == nickname)
    else:
        query = select(Performers)
    
    return session.execute(query).fetchall()

def get_tracks(session: sessionmaker, track_title=None):
    if track_title:
        query = select(Tracks).where(Tracks.track_title == track_title)
    else:
        query = select(Tracks)
    
    return session.execute(query).fetchall()

def get_disks(session: sessionmaker, disk_id=None):
    if disk_id:
        query = select(Disks).where(Disks.disk_id == disk_id)
    else:
        query = select(Disks)
    
    return session.execute(query).fetchall()

def get_strings(session: sessionmaker, string_id=None, limit=5):
    if string_id:
        query = select(Strings).where(Strings.string_id >= string_id).limit(limit)
    else:
        query = select(Strings).limit(5)
    return session.execute(query).fetchall()