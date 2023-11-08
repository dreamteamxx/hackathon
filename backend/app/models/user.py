from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import DateTime, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import func

from app.db import Base
from app.schemas.user import UserRead


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    surname: Mapped[str] = mapped_column(String(length=50), nullable=False)
    login: Mapped[str] = mapped_column(
        String(length=32), unique=True, index=True, nullable=False
    )
    phone: Mapped[str] = mapped_column(Integer, unique=True, index=True, nullable=True)
    birth_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    is_admin: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="false"
    )
    is_editor: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="false"
    )
    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"

    def to_dto(self) -> UserRead:
        return UserRead.model_validate(self)
