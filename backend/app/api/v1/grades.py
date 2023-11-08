import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.schemas import GradeRead

router = APIRouter(prefix="/grades")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[GradeRead])
async def get_grades(
    response: Response,
    session: SessionDB,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    logger.info(f"Getting grades")
    return []
