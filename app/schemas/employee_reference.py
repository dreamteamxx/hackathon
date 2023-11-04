from pydantic import BaseModel, ConfigDict

from app.schemas import GradeRead


class EmployeeReferenceCreate(BaseModel):
    employee_name: str
    grade_id: int
    office_id: int


class EmployeeReferenceUpdate(EmployeeReferenceCreate):
    ...


class EmployeeReferenceRead(EmployeeReferenceCreate):
    id: int
    grade: GradeRead

    model_config = ConfigDict(from_attributes=True)
