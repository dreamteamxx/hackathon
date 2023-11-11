import logging
from typing import Any, Annotated

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models import Condition
from app.repositories.condition import ConditionRepo
from app.schemas import ConditionRead, ConditionUpdate, ConditionCreate

router = APIRouter(prefix="/conditions")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=list[ConditionRead])
async def get_conditions(
    response: Response,
    session: SessionDB,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    condition_repo: ConditionRepo = ConditionRepo(session)
    conditions = await condition_repo.get_conditions()
    if not conditions:
        logger.info(f"Conditions not found")
        return []
    return conditions


@router.post("", response_model=ConditionRead)
async def create_condition(
    session: SessionDB,
    condition_in: ConditionCreate,
) -> Any:
    condition = Condition(**condition_in.model_dump())
    condition_repo: ConditionRepo = ConditionRepo(session)
    condition = await condition_repo.create_condition(condition)
    logger.info(f"Condition created")
    return condition


@router.patch("/{condition_id}", response_model=ConditionUpdate)
async def update_condition(
    condition_id: int,
    response: Response,
    session: SessionDB,
    condition: ConditionCreate,
) -> Any:
    condition_repo: ConditionRepo = ConditionRepo(session)
    condition_object = ConditionUpdate(**condition.model_dump())
    condition = await condition_repo.update_condition(condition_id, condition_object)

    logger.info(f"Condition updated")
    return condition


@router.delete("/{condition_id}", response_model=ConditionRead)
async def delete_condition(
    condition_id: int,
    response: Response,
    session: SessionDB,
) -> Any:
    condition_repo: ConditionRepo = ConditionRepo(session)
    condition = await condition_repo.delete_condition(condition_id)

    logger.info(f"Condition deleted")
    return condition
