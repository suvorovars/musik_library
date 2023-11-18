from sqlalchemy import create_engine, Column, Integer, String, DateTime
from db.tables.db import DeclarativeBase
from sqlalchemy.orm import relationship


class Genres(DeclarativeBase):
    __tablename__ = 'genres'

    genre_id = Column("genre_id", Integer, autoincrement=True, primary_key=True)
    #string = relationship("strings", "genre")
    genre_name = Column("name", String)

    def __init__ (self, genre_name):
        self.genre_name = genre_name
    
