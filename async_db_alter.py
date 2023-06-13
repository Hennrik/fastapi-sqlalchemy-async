import contextlib
import uuid
from datetime import datetime
from sqlalchemy import select

import asyncio
import time

from source.db import Store
from source.db.dependencies import AsyncSessionLocal
from source.schemas.books import BookDTO
from source.schemas.stores import StoreDTO


@contextlib.asynccontextmanager
async def get_async_db_session_manager():
    db_session = AsyncSessionLocal()
    try:
        yield db_session
    except Exception as ex:
        await db_session.rollback()
        raise ex
    finally:
        await db_session.close()


start_time = time.time()


async def get_stores() -> int:
    starting_time = datetime.now()
    print(f"starting getting stores time: {datetime.now()}")
    stmt = select(Store).order_by(Store.name)
    async with get_async_db_session_manager() as session:
        result = await session.execute(stmt)
    print(f"get_stores db duration is: {datetime.now() - starting_time}")

    stores = result.scalars().all()
    print(f"ending get_stores time: {datetime.now()}")

    return len(stores)


async def create_books(books_num: int) -> int:
    starting_time = datetime.now()

    print(f"starting create_books time: {starting_time}")
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


    end_cpu_time = datetime.now()
    print(f"creating books CPU duration: {end_cpu_time - starting_time}")

    # created_books = CrudBook.create_book_service(new_books)

    # print(f"creating books DB duration: {datetime.now() - end_cpu_time}")

    print(f"ending create_books time: {datetime.now()}")

    return len(new_books)


async def main():

    tasks = []
    tasks.append(asyncio.ensure_future(get_stores()))
    tasks.append(asyncio.ensure_future(create_books(100000)))

    counts = await asyncio.gather(*tasks)
    for count in counts:
        print(count)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
