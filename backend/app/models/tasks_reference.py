from typing import List

from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import schemas
from app.db import Base


class TasksReference(Base):
    __tablename__ = "task_reference"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    task_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    execution_time: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="Execution time in seconds"
    )
    conditions: Mapped[List["Condition"]] = relationship()
    min_employee_level: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dto(self) -> schemas.TasksReferenceRead:
        return schemas.TasksReferenceRead.model_validate(self)
