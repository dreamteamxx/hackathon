from pydantic import BaseModel, ConfigDict

from app import schemas


class EmployeeReferenceCreate(BaseModel):
    employee_name: str
    grade_id: int
    office_id: int


class EmployeeReferenceUpdate(EmployeeReferenceCreate):
    ...


class EmployeeReferenceRead(EmployeeReferenceCreate):
    id: int
    grade: schemas.GradeRead
    office: schemas.OfficeRead

    model_config = ConfigDict(from_attributes=True)
