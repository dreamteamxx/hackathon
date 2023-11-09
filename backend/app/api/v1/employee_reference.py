import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.models import EmployeeReference
from app.repositories.employee_reference import EmployeeReferenceRepo
from app.repositories.grade import GradeRepo
from app.repositories.office import OfficeRepo
from app.schemas import EmployeeReferenceRead, EmployeeReferenceCreate, EmployeeReferenceUpdate

router = APIRouter(prefix="/employees")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[EmployeeReferenceRead])
async def get_employees(
        response: Response,
        session: SessionDB,
        skip: int = 0,
        limit: int = 100,
) -> Any:
    employee_reference_repo: EmployeeReferenceRepo = EmployeeReferenceRepo(session)
    employees = await employee_reference_repo.get_employees()
    if not employees:
        logger.info(f"Employees not found")
        return []
    return employees


@router.post("", response_model=EmployeeReferenceRead)
async def create_employee(
        session: SessionDB,
        employee: EmployeeReferenceCreate,
) -> Any:
    employee_reference = EmployeeReference(**employee.model_dump())
    employee_reference_repo: EmployeeReferenceRepo = EmployeeReferenceRepo(session)
    result = await employee_reference_repo.create_employee(employee_reference)
    logger.info(f"Employee created")
    return result


@router.patch("/{employee_id}", response_model=EmployeeReferenceUpdate)
async def update_employee(
        employee_id: int,
        response: Response,
        session: SessionDB,
        employee: EmployeeReferenceUpdate,
) -> Any:
    employee_reference_repo: EmployeeReferenceRepo = EmployeeReferenceRepo(session)
    result = await employee_reference_repo.update_employee(employee_id, employee)
    logger.info(f"Employee updated")
    return result


@router.delete("/{employee_id}")
async def delete_employee(
        employee_id: int,
        response: Response,
        session: SessionDB,
) -> Any:
    employee_reference_repo: EmployeeReferenceRepo = EmployeeReferenceRepo(session)
    await employee_reference_repo.delete_employee(employee_id)
    logger.info(f"Employee deleted")
