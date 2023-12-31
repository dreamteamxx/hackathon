import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models import Office
from app.repositories.office import OfficeRepo
from app.schemas import OfficeRead, OfficeCreate, OfficeUpdate

router = APIRouter(prefix="/offices")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[OfficeRead])
async def get_offices(
    response: Response,
    session: SessionDB,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    office_repo: OfficeRepo = OfficeRepo(session)
    offices = await office_repo.get_offices()
    if not offices:
        logger.info(f"Offices not found")
        return []
    return offices


@router.post("", response_model=OfficeRead)
async def create_office(
    session: SessionDB,
    office: OfficeCreate,
) -> Any:
    office = Office(**office.model_dump())
    office_repo: OfficeRepo = OfficeRepo(session)
    office = await office_repo.create_office(office)
    logger.info(f"Office created")
    return office


@router.patch("/{office_id}", response_model=OfficeUpdate)
async def update_office(
    office_id: int,
    response: Response,
    session: SessionDB,
    office: OfficeUpdate,
) -> Any:
    office_repo: OfficeRepo = OfficeRepo(session)
    office_object = OfficeUpdate(**office.model_dump())
    office = await office_repo.update_office(office_id, office_object)

    logger.info(f"Office updated")
    return office


@router.delete("/{office_id}")
async def delete_office(
    office_id: int,
    response: Response,
    session: SessionDB,
) -> Any:
    office_repo: OfficeRepo = OfficeRepo(session)
    await office_repo.delete_office(office_id)
    logger.info(f"Office deleted")
