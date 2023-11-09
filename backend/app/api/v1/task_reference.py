import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models import TasksReference
from app.repositories.task_reference import TaskReferenceRepo
from app.schemas import TasksReferenceRead, TasksReferenceCreate, TasksReferenceUpdate

router = APIRouter(prefix="/tasks_reference")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[TasksReferenceRead])
async def get_tasks_reference(
        response: Response,
        session: SessionDB,
        skip: int = 0,
        limit: int = 100,
) -> Any:
    task_reference_repo: TaskReferenceRepo = TaskReferenceRepo(session)
    tasks_reference = await task_reference_repo.get_tasks_references()
    if not tasks_reference:
        logger.info(f"TasksReference not found")
        return []
    return tasks_reference


@router.post("", response_model=TasksReferenceRead)
async def create_task_reference(
        session: SessionDB,
        task_reference: TasksReferenceCreate,
) -> Any:
    task_reference = TasksReference(**task_reference.model_dump())
    task_reference_repo: TaskReferenceRepo = TaskReferenceRepo(session)
    task_reference = await task_reference_repo.create_task_reference(task_reference)
    logger.info(f"TaskReference created")
    return task_reference


@router.patch("/{task_reference_id}", response_model=TasksReferenceUpdate)
async def update_task_reference(
        task_reference_id: int,
        response: Response,
        session: SessionDB,
        task_reference: TasksReferenceUpdate,
) -> Any:
    task_reference_repo: TaskReferenceRepo = TaskReferenceRepo(session)
    await task_reference_repo.update_task_reference(task_reference_id, task_reference)
    logger.info(f"TaskReference updated")


@router.delete("/{task_reference_id}")
async def delete_task_reference(
        task_reference_id: int,
        response: Response,
        session: SessionDB,
) -> Any:
    task_reference_repo: TaskReferenceRepo = TaskReferenceRepo(session)
    await task_reference_repo.delete_task_reference(task_reference_id)
    logger.info(f"TaskReference deleted")
