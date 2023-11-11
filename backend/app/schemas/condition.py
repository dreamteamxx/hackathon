from pydantic import BaseModel, ConfigDict


class ConditionCreate(BaseModel):
    name: str
    task_id: int


class ConditionUpdate(ConditionCreate):
    ...


class ConditionRead(ConditionCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
