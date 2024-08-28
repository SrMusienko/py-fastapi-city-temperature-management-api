from pydantic import BaseModel


class CityBase(BaseModel):
    id: int
    name: str
    additional: str


class CityCreate(BaseModel):
    name: str
    additional: str
