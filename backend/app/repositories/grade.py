import logging
from typing import Optional

from fastapi import HTTPException

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import GradeRead, GradeCreate, GradeUpdate
from app.models import Grade

logger = logging.getLogger(__name__)


class GradeRepo(SQLAlchemyRepo):

    async def get_grade(self, grade_id: int) -> Optional[GradeRead]:
        query = await self.session.execute(
            select(models.Grade).where(models.Grade.id == grade_id)
        )
        result = query.scalars().first()
        return result.to_dto() if result else None

    async def get_grades(self) -> list[GradeRead] | None:
        stmt = await self.session.scalars(select(models.Grade))
        result = stmt.all()
        return list(map(models.Grade.to_dto, result)) if result else None

    async def create_grade(self, grade: Grade) -> Grade:
        try:
            self.session.add(grade)
            await self.session.commit()
            return grade

        except Exception as e:
            logger.error(f"Error creating grade: {e}")
            await self.session.rollback()

    async def update_grade(self, grade_id: int, grade_new: GradeUpdate) -> GradeUpdate:
        stmt = update(Grade).where(Grade.id == grade_id).values(**grade_new.model_dump())
        await self.session.execute(stmt)
        await self.session.commit()
        return grade_new

    async def delete_grade(self, grade_id: int) -> None:
        stmt = delete(models.Grade).where(models.Grade.id == grade_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting grade: {e}")
            await self.session.rollback()
