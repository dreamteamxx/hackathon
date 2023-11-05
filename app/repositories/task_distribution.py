import logging

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import TaskDistributionCreate, TaskDistributionRead, TaskDistributionUpdate

logger = logging.getLogger(__name__)


class TaskDistributionRepo(SQLAlchemyRepo):
    async def get_task_distributions(self) -> list[TaskDistributionRead] | None:
        stmt = await self.session.scalars(select(models.TaskDistribution))
        result = await stmt.all()
        return list(map(models.TaskDistribution.to_dto, result)) if result else None

    async def create_task_distribution(self, task_distribution: TaskDistributionCreate) -> None:
        stmt = insert(models.TaskDistribution).values(**task_distribution.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error creating task_distribution: {e}")
            await self.session.rollback()

    async def update_task_distribution(self, task_distribution_id, task_distribution: TaskDistributionUpdate) -> None:
        stmt = update(models.TaskDistribution).where(models.TaskDistribution.id == task_distribution_id).values(
            **task_distribution.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error updating task_distribution: {e}")
            await self.session.rollback()

    async def delete_task_distribution(self, task_distribution_id: int) -> None:
        stmt = delete(models.TaskDistribution).where(models.TaskDistribution.id == task_distribution_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error deleting task_distribution: {e}")
            await self.session.rollback()
