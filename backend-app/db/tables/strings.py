from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from db.tables.db import DeclarativeBase
from sqlalchemy.orm import relationship

class Strings(DeclarativeBase):
    __tablename__ = 'strings'

    string_id = Column("string_id", Integer, autoincrement=True, primary_key=True)
    disk_fk = Column(Integer, ForeignKey("disks.disk_id"))
    #disk = relationship("disks", back_populates="strings")
    performer_fk = Column(Integer, ForeignKey("performers.performer_id"))
    #performer = relationship("performers", back_populates="strings")
    track_fk = Column(Integer, ForeignKey("tracks.track_id"))
    #track = relationship("tracks", back_populates="strings")
    genre_fk = Column(Integer, ForeignKey("genres.genre_id"))
    #genre = relationship("genres", back_populates="strings")
    string_num = Column("num", Integer)

    def __init__ (self, string_id, disk_fk, performer_fk, track_fk, genre_fk, string_num):
        self.string_id = string_id
        self.disk_fk = disk_fk
        self.performer_fk = performer_fk
        self.track_fk = track_fk
        self.genre_fk = genre_fk
        self.string_num = string_num


        