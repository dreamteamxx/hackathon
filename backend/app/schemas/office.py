from pydantic import BaseModel, ConfigDict


class OfficeCreate(BaseModel):
    office_name: str
    address: str


class OfficeUpdate(OfficeCreate):
    ...


class OfficeRead(OfficeCreate):
    id: int
    coordinates: str | None = None
    model_config = ConfigDict(from_attributes=True)
