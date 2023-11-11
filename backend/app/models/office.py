from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app import schemas
from app.db import Base


class Office(Base):
    __tablename__ = "office"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False, autoincrement=True
    )
    office_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    coordinates: Mapped[str] = mapped_column(String, nullable=True)

    def to_dto(self) -> schemas.OfficeRead:
        return schemas.OfficeRead.model_validate(self)
