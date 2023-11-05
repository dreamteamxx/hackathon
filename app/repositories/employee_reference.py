import logging

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import EmployeeReferenceRead, EmployeeReferenceCreate, EmployeeReferenceUpdate


class EmployeeReferenceRepo(SQLAlchemyRepo):

    async def get_employees(self) -> list[EmployeeReferenceRead] | None:
        stmt = await self.session.scalars(select(models.EmployeeReference))
        result = await stmt.all()
        return list(map(models.EmployeeReference.to_dto, result)) if result else None

    async def create_employee(self, employee_reference: EmployeeReferenceCreate) -> None:
        stmt = insert(models.EmployeeReference).values(**employee_reference.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logging.error(f"Error creating employee_reference: {e}")
            await self.session.rollback()

    async def update_employee(self, employee_reference_id: int,
                              employee_reference: EmployeeReferenceUpdate) -> None:
        stmt = update(models.EmployeeReference).where(models.EmployeeReference.id == employee_reference_id).values(
            **employee_reference.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logging.error(f"Error updating employee_reference: {e}")
            await self.session.rollback()

    async def delete_employee(self, employee_reference_id: int) -> None:
        stmt = delete(models.EmployeeReference).where(models.EmployeeReference.id == employee_reference_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logging.error(f"Error deleting employee_reference: {e}")
            await self.session.rollback()
