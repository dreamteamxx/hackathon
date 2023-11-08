import logging

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import GradeRead, GradeCreate, GradeUpdate

logger = logging.getLogger(__name__)


class GradeRepo(SQLAlchemyRepo):

    async def get_grade(self, grade_id: int) -> GradeRead | None:
        stmt = await self.session.scalars(select(models.Grade).where(models.Grade.id == grade_id))
        result = await stmt.first()
        return models.Grade.to_dto(result) if result else None

    async def get_grades(self) -> list[GradeRead] | None:
        stmt = await self.session.scalars(select(models.Grade))
        result = await stmt.all()
        return list(map(models.Grade.to_dto, result)) if result else None

    async def create_grade(self, grade: GradeCreate) -> None:

        try:
            self.session.add(grade)
            await self.session.commit()
            return await self.get_grade(grade.id)
        except Exception as e:
            logger.error(f"Error creating grade: {e}")
            await self.session.rollback()

    async def update_grade(self, grade_id: int, grade: GradeUpdate) -> None:
        item = await self.get_grade(grade_id)
        if not grade:
            return None
        self.session.merge(grade)
        await self.session.commit()
        return item

    async def delete_grade(self, grade_id: int) -> None:
        stmt = delete(models.Grade).where(models.Grade.id == grade_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting grade: {e}")
            await self.session.rollback()
