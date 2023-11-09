import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models import TaskDistribution
from app.repositories.task_distribution import TaskDistributionRepo
from app.schemas import TaskDistributionRead, TaskDistributionCreate, TaskDistributionUpdate

router = APIRouter(prefix="/task_distributions")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[TaskDistributionRead])
async def get_task_distributions(
        response: Response,
        session: SessionDB,
        skip: int = 0,
        limit: int = 100,
) -> Any:
    task_distribution_repo: TaskDistributionRepo = TaskDistributionRepo(session)
    task_distributions = await task_distribution_repo.get_task_distributions()
    if not task_distributions:
        logger.info(f"TaskDistributions not found")
        return []
    return task_distributions


@router.post("", response_model=TaskDistributionRead)
async def create_task_distribution(
        session: SessionDB,
        task_distribution: TaskDistributionCreate,
) -> Any:
    task_distribution_repo: TaskDistributionRepo = TaskDistributionRepo(session)
    task_distribution = TaskDistribution(**task_distribution.model_dump())
    task_distribution = await task_distribution_repo.create_task_distribution(task_distribution)
    logger.info(f"TaskDistribution created")
    return task_distribution


@router.patch("/{task_distribution_id}", response_model=TaskDistributionUpdate)
async def update_task_distribution(
        task_distribution_id: int,
        response: Response,
        session: SessionDB,
        task_distribution: TaskDistributionUpdate,
) -> Any:
    task_distribution_repo: TaskDistributionRepo = TaskDistributionRepo(session)
    await task_distribution_repo.update_task_distribution(task_distribution_id, task_distribution)
    logger.info(f"TaskDistribution updated")


@router.delete("/{task_distribution_id}")
async def delete_task_distribution(
        task_distribution_id: int,
        response: Response,
        session: SessionDB,
) -> Any:
    task_distribution_repo: TaskDistributionRepo = TaskDistributionRepo(session)
    await task_distribution_repo.delete_task_distribution(task_distribution_id)
    logger.info(f"TaskDistribution deleted")
