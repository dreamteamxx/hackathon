from datetime import datetime

from sqlalchemy import String, BigInteger, Boolean, func, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class Point(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    point_address: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
    carts_added: Mapped[bool] = mapped_column(Boolean, server_default="false", default=False)
    days_count_after_delivery: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    applications_count: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    carts_count: Mapped[int] = mapped_column(Integer, nullable=True, default=0)

    def to_dto(self) -> schemas.PointRead:
        return schemas.PointRead.model_validate(self)
