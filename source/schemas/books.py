from pydantic import BaseModel


class BookDTO(BaseModel):
    isbn: str
    full_name: str
    author: str

    class Config:
        orm_mode = True
