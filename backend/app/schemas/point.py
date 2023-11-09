from pydantic import BaseModel, ConfigDict


class PointCreate(BaseModel):
    point_address: str


class PointUpdate(PointCreate):
    ...


class PointRead(PointCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
