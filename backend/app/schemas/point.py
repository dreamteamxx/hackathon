from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PointCreate(BaseModel):
    point_address: str
    created_at: datetime
    carts_added: bool
    days_count_after_delivery: int
    applications_count: int
    carts_count: int


class PointUpdate(PointCreate):
    ...


class PointRead(PointCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
