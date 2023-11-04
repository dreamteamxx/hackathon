from pydantic import BaseModel, ConfigDict


class TasksReferenceCreate(BaseModel):
    task_name: str
    priority: int
    execution_time: int
    condition_1: str
    condition_2: str
    min_employee_level: int


class TasksReferenceUpdate(TasksReferenceCreate):
    ...


class TasksReferenceRead(TasksReferenceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
