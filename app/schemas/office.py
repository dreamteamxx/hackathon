from pydantic import BaseModel, ConfigDict


class OfficeCreate(BaseModel):
    office_name: str
    address: str


class OfficeUpdate(OfficeCreate):
    ...


class OfficeRead(OfficeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
