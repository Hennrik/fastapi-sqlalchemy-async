from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from source.core.config import settings

# base class for all database models
Base = declarative_base()

async_engine = create_async_engine(settings.DB_CONNECTION_URL)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_db_session() -> AsyncIterator[AsyncSession]:
    db_session = AsyncSessionLocal()
    try:
        yield db_session
    except Exception as ex:
        await db_session.rollback()
        raise ex
    finally:
        await db_session.close()
