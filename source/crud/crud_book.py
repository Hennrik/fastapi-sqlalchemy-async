import logging
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from source.db import Book
from source.schemas.books import BookDTO

logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S:%f', level=logging.INFO)

logger = logging.getLogger(__file__)


class CrudBook:
    @staticmethod
    def create_book_service(books: list[BookDTO]) -> list[Book]:
        start_time = datetime.now()
        objs_in_data = map(lambda obj_in: jsonable_encoder(obj_in), books)
        db_objs = [Book(**obj_in_data) for obj_in_data in objs_in_data]
        # db.add_all(db_objs)
        end_cpu_time = datetime.now()
        logger.warning(f"inner book cpu time {end_cpu_time - start_time}")
        # await db.commit()
        logger.warning(f"inner book db time {datetime.now() - end_cpu_time}")
        return db_objs
