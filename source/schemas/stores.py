from pydantic import BaseModel


class StoreDTO(BaseModel):
    name: str
    address: str
    city: str

    class Config:
        orm_mode = True
