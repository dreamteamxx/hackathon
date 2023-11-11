import logging
from typing import Optional

from fastapi import HTTPException

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import ConditionUpdate, ConditionRead, ConditionCreate
from app.models import Condition

logger = logging.getLogger(__name__)


class ConditionRepo(SQLAlchemyRepo):
    async def get_condition(self, condition_id: int) -> Optional[ConditionRead]:
        query = await self.session.execute(
            select(models.Condition).where(models.Condition.id == condition_id)
        )
        result = query.scalars().first()
        return result.to_dto() if result else None

    async def get_conditions(self) -> list[ConditionRead] | None:
        stmt = await self.session.scalars(select(models.Condition))
        result = stmt.all()
        return list(map(models.Condition.to_dto, result)) if result else None

    async def create_condition(self, condition: Condition) -> Condition:
        try:
            self.session.add(condition)
            await self.session.commit()
            return condition

        except Exception as e:
            logger.error(f"Error creating condition: {e}")
            await self.session.rollback()

    async def update_condition(
        self, condition_id: int, condition_new: ConditionUpdate
    ) -> ConditionUpdate:
        stmt = (
            update(Condition)
            .where(Condition.id == condition_id)
            .values(**condition_new.model_dump())
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return condition_new

    async def delete_condition(self, condition_id: int) -> None:
        stmt = delete(models.Condition).where(models.Condition.id == condition_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting condition: {e}")
            await self.session.rollback()
