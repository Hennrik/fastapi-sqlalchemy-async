import logging
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from source.crud.crud_book import CrudBook
from source.db import Book
from source.db.dependencies import get_async_db_session
from source.schemas.books import BookDTO

router = APIRouter()

logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S:%f', level=logging.INFO)

logger = logging.getLogger(__file__)


@router.get("/book/", response_model=list[BookDTO])
async def get_books(
        db: AsyncSession = Depends(get_async_db_session),
) -> list[BookDTO]:
    logger.warning(f"starting get_books time: {datetime.now()}")
    stmt = select(Book).order_by(Book.author).limit(1000000)
    result = await db.execute(stmt)

    books = result.scalars().all()

    logger.warning(f"ending get_books time: {datetime.now()}")

    return [BookDTO.from_orm(book) for book in books[-100:]]


@router.get("/hello")
def hello() -> str:
    return "Greetings"


@router.post("/book/", response_model=int)
async def create_books(
        books_num: int,
        # db: AsyncSession = Depends(get_async_db_session)
) -> int:
    start_time = datetime.now()

    logger.warning(f"starting create_books time: {start_time}")
    # new_books = []
    # for i in range(books_num):
    #     book = BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}")
    #     new_books.append(book)
    #
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]

    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]

    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]
    new_books = [
        BookDTO(isbn=str(uuid.uuid4()), full_name=f"book_name_{i}", author=f"author_{i}") for i in
        range(books_num)
    ]

    end_cpu_time = datetime.now()
    logger.warning(f"creating books CPU duration: {end_cpu_time - start_time}")

    # created_books = CrudBook.create_book_service(new_books)

    # logger.warning(f"creating books DB duration: {datetime.now() - end_cpu_time}")

    logger.warning(f"ending create_books time: {datetime.now()}")

    return len(new_books)
