from sqlalchemy import Column, Integer, String

from source.db.dependencies import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    author = Column(String, nullable=False)
