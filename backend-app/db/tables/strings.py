from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .default import SqlAlchemyBase


class Strings(SqlAlchemyBase):
    __tablename__ = "strings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    disk_fk: Mapped[int] = mapped_column(ForeignKey("disks.disk_id"))
    disk: Mapped[List['Disks']] = relationship(back_populates="string")

    string_number: Mapped[int] = mapped_column(nullable=False)
    track_fk: Mapped[int] = mapped_column(ForeignKey("tracks.track_id"))
    track: Mapped[List['Tracks']] = relationship("Tracks", back_populates="string")

    performer_fk: Mapped[int] = mapped_column(ForeignKey("performers.performer_id"))
    performer: Mapped[List["Performers"]] = relationship( back_populates="string")

    genre_fk: Mapped[int] = mapped_column(ForeignKey("genres.genre_id"))
    genre: Mapped[List["Genres"]] = relationship( back_populates="string")

    duration: Mapped[int] = mapped_column(nullable=False)
