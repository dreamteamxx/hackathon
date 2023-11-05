import logging

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import GradeRead, GradeCreate, GradeUpdate

logger = logging.getLogger(__name__)


class GradeRepo(SQLAlchemyRepo):
    async def get_grades(self) -> list[GradeRead] | None:
        stmt = await self.session.scalars(select(models.Grade))
        result = await stmt.all()
        return list(map(models.Grade.to_dto, result)) if result else None

    async def create_grade(self, grade: GradeCreate) -> None:
        stmt = insert(models.Grade).values(**grade.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error creating grade: {e}")
            await self.session.rollback()

    async def update_grade(self, grade: GradeUpdate) -> None:
        stmt = update(models.Grade).where(models.Grade.id == grade.id).values(**grade.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error updating grade: {e}")
            await self.session.rollback()
