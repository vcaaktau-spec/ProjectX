from pydantic import BaseModel


class CompanyResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
