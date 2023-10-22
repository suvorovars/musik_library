from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .db_session import SqlAlchemyBase

class Disks(SqlAlchemyBase):
    __tablename__ = "disks"
    disk_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    string: Mapped["Strings"] = relationship( back_populates="disk")

    disk_title: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)