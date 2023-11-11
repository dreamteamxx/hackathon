from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class Condition(Base):
    __tablename__ = "condition"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_reference.id", ondelete="CASCADE"), nullable=False
    )

    def to_dto(self) -> schemas.ConditionRead:
        return schemas.ConditionRead.model_validate(self)
