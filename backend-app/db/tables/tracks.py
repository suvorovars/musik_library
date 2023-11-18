from sqlalchemy import create_engine, Column, Integer, String, DateTime
from db.tables.db import DeclarativeBase
from sqlalchemy.orm import relationship


class Tracks(DeclarativeBase):
    __tablename__ = 'tracks'

    track_id = Column("track_id", Integer, autoincrement=True, primary_key=True)
    #string = relationship("strings", 'track')
    track_title = Column("title", String)

    def __init__ (self, track_title):
        self.track_title = track_title