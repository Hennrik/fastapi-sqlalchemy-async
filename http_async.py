import contextlib
from datetime import datetime
from sqlalchemy import select

import aiohttp
import asyncio
import time

from source.db import Store
from source.db.dependencies import AsyncSessionLocal
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


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def get_stores(
        session
) -> list[StoreDTO]:
    starting_time = datetime.now()
    print(f"starting getting stores time: {datetime.now()}")
    stmt = select(Store).order_by(Store.name)

    result = await session.execute(stmt)
    print(f"get_stores db duration is: {datetime.now() - starting_time}")

    stores = result.scalars().all()
    print(f"ending get_stores time: {datetime.now()}")

    return [StoreDTO.from_orm(store) for store in stores[-100:]]


# async def main():
#
#     async with aiohttp.ClientSession() as session:
#
#         tasks = []
#         for number in range(1, 151):
#             url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#             tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
#
#         original_pokemon = await asyncio.gather(*tasks)
#         for pokemon in original_pokemon:
#             print(pokemon)


async def main():
    async with get_async_db_session_manager() as session:

        tasks = []
        for _ in range(2):
            # url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_stores(session)))

        stores = await asyncio.gather(*tasks)
        for store in stores:
            print(len(store))


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
