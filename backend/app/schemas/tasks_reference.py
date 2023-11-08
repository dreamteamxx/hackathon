from typing import List

from pydantic import BaseModel, ConfigDict

from app.schemas import ConditionRead, ConditionCreate


class TasksReferenceCreate(BaseModel):
    task_name: str
    priority: int
    execution_time: int
    conditions: List[ConditionCreate | ConditionRead]
    min_employee_level: int


class TasksReferenceUpdate(TasksReferenceCreate):
    ...


class TasksReferenceRead(TasksReferenceCreate):
    id: int
    conditions: List[ConditionRead]

    model_config = ConfigDict(from_attributes=True)
