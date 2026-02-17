from pydantic import BaseModel
from typing import Optional


class ComplaintCreate(BaseModel):
    bus_id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    description: str


class ComplaintResponse(BaseModel):
    id: int
    bus_id: int
    name: Optional[str]
    phone: Optional[str]
    description: str
    status: str

    class Config:
        orm_mode = True