import logging
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from source.crud.crud_store import CrudStore
from source.db import Store
from source.db.dependencies import get_async_db_session
from source.schemas.stores import StoreDTO

router = APIRouter()

logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S:%f', level=logging.INFO)

logger = logging.getLogger(__file__)


@router.get("/store/", response_model=list[StoreDTO])
async def get_stores(
        db: AsyncSession = Depends(get_async_db_session),
) -> list[StoreDTO]:
    start_time = datetime.now()
    logger.warning(f"starting getting stores time: {datetime.now()}")
    stmt = select(Store).order_by(Store.name)

    result = await db.execute(stmt)
    logger.warning(f"get_stores db duration is: {datetime.now() - start_time}")

    stores = result.scalars().all()

    logger.warning(f"ending get_stores time: {datetime.now()}")

    return [StoreDTO.from_orm(store) for store in stores[-100:]]


@router.post("/store/", response_model=int)
async def create_stores(
        stores_num: int,
        db: AsyncSession = Depends(get_async_db_session)
) -> int:
    start_time = datetime.now()
    logger.warning(f"starting create_stores time: {start_time}")

    new_stores = [
        StoreDTO(name=f"store_name_{uuid.uuid4()}", city=f"city_{i}", address=f"address_{i}") for i in
        range(stores_num)
    ]

    end_cpu_time = datetime.now()

    logger.warning(f"creating stores CPU duration: {end_cpu_time - start_time}")

    created_stored = await CrudStore.create_store_service(new_stores, db)

    logger.warning(f"ending create_stores time: {datetime.now()}")

    return len(created_stored)
