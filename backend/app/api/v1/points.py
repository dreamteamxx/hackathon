import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models.points import Point
from app.schemas import PointRead

router = APIRouter(prefix="/points")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[PointRead])
async def get_points(
        response: Response,
        session: SessionDB,
        skip: int = 0,
        limit: int = 100,
) -> Any:
    return Point


@router.post("", response_model=PointRead)
async def create_point(
        session: SessionDB,
        point: PointRead,
) -> Any:
    return point


@router.patch("/{point_id}", response_model=PointRead)
async def update_point(
        point_id: int,
        response: Response,
        session: SessionDB,
        point: PointRead,
) -> Any:
    return point


@router.delete("/{point_id}", response_model=PointRead)
async def delete_point(
        point_id: int,
        response: Response,
        session: SessionDB,
        point: PointRead,
) -> Any:
    return
