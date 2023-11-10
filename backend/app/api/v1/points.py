import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models.points import Point
from app.repositories.point import PointRepo

from app.schemas import PointRead, PointCreate, PointUpdate

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
    point_repo: PointRepo = PointRepo(session)
    points = await point_repo.get_points()
    if not points:
        logger.info(f"Points not found")
        return []
    return points


@router.post("", response_model=PointRead)
async def create_point(
        session: SessionDB,
        point: PointCreate,
) -> Any:
    point = Point(**point.model_dump())
    point_repo: PointRepo = PointRepo(session)
    point = await point_repo.create_point(point)
    logger.info(f"Point created")
    return point


@router.patch("/{point_id}", response_model=PointUpdate)
async def update_point(
        point_id: int,
        response: Response,
        session: SessionDB,
        point: PointRead,
) -> Any:
    point_repo: PointRepo = PointRepo(session)
    point_object = PointUpdate(**point.model_dump())
    point = await point_repo.update_point(point_id, point_object)

    logger.info(f"Point updated")
    return point


@router.delete("/{point_id}")
async def delete_point(
        point_id: int,
        response: Response,
        session: SessionDB,
) -> Any:
    point_repo: PointRepo = PointRepo(session)
    await point_repo.delete_point(point_id)
    logger.info(f"Point deleted")
