from sqlalchemy import create_engine, Column, Integer, String, DateTime
from db.tables.db import DeclarativeBase
from sqlalchemy.orm import relationship


class Performers(DeclarativeBase):
    __tablename__ = 'performers'

    performer_id = Column("performer_id", Integer, autoincrement=True, primary_key=True)
    #string = relationship('strings', 'performer')
    performer_nickname = Column("nickname", String)
    
    def __init__(self, performer_nickname):
        self.performer_nickname = performer_nickname