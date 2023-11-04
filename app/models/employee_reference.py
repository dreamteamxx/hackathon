from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import schemas
from app.db import Base


class EmployeeReference(Base):
    __tablename__ = "employee_reference"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    employee_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    grade_id: Mapped[int] = mapped_column(ForeignKey("grade.id", ondelete="CASCADE"), nullable=False)
    office_id: Mapped[int] = mapped_column(ForeignKey("office.id", ondelete="CASCADE"), nullable=False)
    grade: Mapped["Grade"] = relationship()

    def to_dto(self) -> schemas.EmployeeReferenceRead:
        return schemas.EmployeeReferenceRead.model_validate(self)
