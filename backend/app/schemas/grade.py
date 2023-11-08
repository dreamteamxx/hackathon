from pydantic import BaseModel, ConfigDict


class GradeCreate(BaseModel):
    grade_name: str
    grade_level: int


class GradeUpdate(GradeCreate):
    ...


class GradeRead(GradeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
