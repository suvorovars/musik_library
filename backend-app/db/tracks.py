from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .db_session import SqlAlchemyBase

class Tracks(SqlAlchemyBase):
    __tablename__ = "tracks"
    track_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    string: Mapped["Strings"] = relationship(back_populates="track")

    track_title: Mapped[str] = mapped_column(nullable=False)
