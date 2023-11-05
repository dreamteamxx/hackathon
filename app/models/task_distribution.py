from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class TaskDistribution(Base):
    __tablename__ = "task_distribution"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_reference.id", ondelete="CASCADE"), nullable=False
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employee_reference.id", ondelete="CASCADE"), nullable=False
    )

    def to_dto(self) -> schemas.TaskDistributionRead:
        return schemas.TaskDistributionRead.model_validate(self)
