from typing import List

from pydantic import BaseModel, ConfigDict

from app.schemas import ConditionRead, ConditionCreate


class TaskReferenceCreate(BaseModel):
    task_name: str
    priority: int
    execution_time: int
    conditions: List[ConditionCreate | ConditionRead]
    min_employee_level: int


class TaskReferenceUpdate(TaskReferenceCreate):
    ...


class TaskReferenceRead(TaskReferenceCreate):
    id: int
    conditions: None = None

    model_config = ConfigDict(from_attributes=True)
