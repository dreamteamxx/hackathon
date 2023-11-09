from sqlalchemy import String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Point(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    point_number: Mapped[int] = mapped_column(BigInteger, nullable=False, autoincrement=True)
    point_address: Mapped[str] = mapped_column(String, nullable=False)
    when_added: Mapped[str] = mapped_column(String, nullable=True)
    maps_added: Mapped[bool] = mapped_column(Boolean, server_default="false", default=False)
    days_count_after_adding: Mapped[int] = mapped_column(BigInteger, nullable=True)
    applications_count: Mapped[int] = mapped_column(BigInteger, nullable=True)
    maps_count: Mapped[int] = mapped_column(BigInteger, nullable=True)
