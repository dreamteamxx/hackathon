from pydantic import BaseModel, ConfigDict


class TaskDistributionCreate(BaseModel):
    task_id: int
    employee_id: int


class TaskDistributionUpdate(TaskDistributionCreate):
    ...


class TaskDistributionRead(TaskDistributionCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
