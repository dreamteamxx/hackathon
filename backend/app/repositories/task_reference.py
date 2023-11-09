import logging

from sqlalchemy import select, update, delete

from app import models
from app.models import TasksReference
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import TasksReferenceUpdate, TasksReferenceRead

logger = logging.getLogger(__name__)


class TaskReferenceRepo(SQLAlchemyRepo):
    async def get_tasks_references(self) -> list[TasksReferenceRead] | None:
        stmt = await self.session.scalars(select(models.TasksReference))
        result = stmt.all()
        return list(map(models.TasksReference.to_dto, result)) if result else None

    async def create_task_reference(self, task_reference: TasksReference) -> TasksReference:
        try:
            self.session.add(task_reference)
            await self.session.commit()
            return task_reference

        except Exception as e:
            logger.error(f"Error creating task_reference: {e}")
            await self.session.rollback()

    async def update_task_reference(self, task_reference_id,
                                    task_reference: TasksReferenceUpdate) -> TasksReferenceUpdate:
        stmt = update(TasksReference).where(TasksReference.id == task_reference_id).values(
            **task_reference.model_dump())
        await self.session.execute(stmt)
        await self.session.commit()
        return task_reference

    async def delete_task_reference(self, task_reference_id: int) -> None:
        stmt = delete(models.TasksReference).where(models.TasksReference.id == task_reference_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error deleting task_reference: {e}")
            await self.session.rollback()
