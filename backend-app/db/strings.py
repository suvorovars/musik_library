from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db_session import SqlAlchemyBase


class Strings(SqlAlchemyBase):
    __tablename__ = "strings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    disk_fk: Mapped[int] = mapped_column(foreign_key=ForeignKey("disks.disk_id"))
    disk = relationship("Disks", back_populates="strings")

    string_number: Mapped[int] = mapped_column(nullable=False)
    track_fk: Mapped[int] = mapped_column(foreign_key=ForeignKey("tracks.track_id"))
    track = relationship("Tracks", back_populates="strings")

    performer_fk: Mapped[int] = mapped_column(foreign_key=ForeignKey("performers.performer_id"))
    performer = relationship("Performers", back_populates="strings")

    genre_fk: Mapped[int] = mapped_column(foreign_key=ForeignKey("genres.genre_id"))
    genre = relationship("Genres", back_populates="strings")

    duration: Mapped[int] = mapped_column(nullable=False)
