from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .db_session import SqlAlchemyBase

class Genres(SqlAlchemyBase):
    __tablename__ = "genres"
    genre_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    string: Mapped["Strings"] = relationship(back_populates="genre")

    genre_title: Mapped[str] = mapped_column(nullable=False)