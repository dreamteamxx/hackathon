from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    grade_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    grade_level: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dto(self) -> schemas.GradeRead:
        return schemas.GradeRead.model_validate(self)
