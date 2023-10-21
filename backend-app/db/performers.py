from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db_session import SqlAlchemyBase


class Performers(SqlAlchemyBase):
    __tablename__ = "performers"
    performer_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    performer_name: Mapped[str] = mapped_column(nullable=False)