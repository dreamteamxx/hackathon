import logging

from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError

from app import models
from app.models import EmployeeReference
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import (
    EmployeeReferenceRead,
    EmployeeReferenceUpdate,
)


class EmployeeReferenceRepo(SQLAlchemyRepo):
    async def get_employee(
        self, employee_reference_id: int
    ) -> EmployeeReferenceRead | None:
        stmt = await self.session.scalars(
            select(models.EmployeeReference).where(
                models.EmployeeReference.id == employee_reference_id
            )
        )
        result = stmt.first()
        return models.EmployeeReference.to_dto(result) if result else None

    async def get_employees(self) -> list[EmployeeReferenceRead] | None:
        stmt = await self.session.scalars(select(models.EmployeeReference))
        result = stmt.all()
        return list(map(models.EmployeeReference.to_dto, result)) if result else None

    async def create_employee(
        self, employee_reference: EmployeeReference
    ) -> EmployeeReference:
        try:
            self.session.add(employee_reference)
            await self.session.commit()
            return employee_reference
        except Exception as e:
            logging.error(f"Error creating employee_reference: {e}")
            await self.session.rollback()

    async def update_employee(
        self, employee_reference_id: int, employee_reference: EmployeeReferenceUpdate
    ) -> EmployeeReferenceRead | None:
        employee = await self.get_employee(employee_reference_id)
        if not employee:
            return None
        self.session.merge(employee_reference)
        await self.session.commit()
        return employee

    async def delete_employee(self, employee_reference_id: int) -> None:
        stmt = delete(models.EmployeeReference).where(
            models.EmployeeReference.id == employee_reference_id
        )
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logging.error(f"Error deleting employee_reference: {e}")
            await self.session.rollback()
