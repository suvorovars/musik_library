from sqlalchemy import create_engine, Column, Integer, String
from db.tables.db import DeclarativeBase
from sqlalchemy.orm import relationship

class Disks(DeclarativeBase):
    __tablename__ = 'disks'

    disk_id = Column("disk_id", Integer, autoincrement=True, primary_key=True)
    #string = relationship("strings", "disks")
    disk_name = Column("disk_name", String)
    disk_date = Column("date", Integer)

    def __init__ (self, disk_name, disk_date):
        self.genre_name = disk_name
        self.disk_date = disk_date