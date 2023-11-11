from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PointCreate(BaseModel):
    point_address: str
    connected_date: datetime
    cards_delivered: datetime
    days_after_last_delivery: int
    approved_requests_count: int
    issued_cards_count: int


class PointUpdate(PointCreate):
    ...


class PointRead(PointCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
