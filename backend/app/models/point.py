from datetime import datetime

from sqlalchemy import String, BigInteger, func, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class Point(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    point_address: Mapped[str] = mapped_column(String, nullable=False)
    connected_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    cards_delivered: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    days_after_last_delivery: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0
    )
    approved_requests_count: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0
    )
    issued_cards_count: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )

    def to_dto(self) -> schemas.PointRead:
        return schemas.PointRead.model_validate(self)
