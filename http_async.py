import asyncio
import time

import aiohttp
import requests


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def http_performance_async():
    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


async def http_async():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


def http_sync():
    for number in range(1, 151):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'])


if __name__ == '__main__':
    start_time = time.time()
    # http_sync()
    # asyncio.run(http_performance_async())
    asyncio.run(http_async())
    print("--- %s seconds ---" % (time.time() - start_time))
