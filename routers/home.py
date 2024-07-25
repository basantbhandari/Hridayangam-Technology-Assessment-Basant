import asyncio
import aiohttp

from fastapi import APIRouter
from pokeapi.get_all_pokemon import fetch_all_pokemon, build_pokemons_items
from database.operations import insert_or_update_data
from data.process import build_all_pokemon_data
from database.query import insert_and_update_pokemon_details_query

home_router = APIRouter()


async def populate_pokemons_async() -> None:
    async with aiohttp.ClientSession() as session:
        all_pokemon = await fetch_all_pokemon(session)
        if all_pokemon:
            raw_result = await build_pokemons_items(all_pokemon)
            result = build_all_pokemon_data(raw_result)
            await insert_or_update_data(insert_and_update_pokemon_details_query, result)


@home_router.get('/')
def populate_pokemons():
    asyncio.run(populate_pokemons_async())

    return {"message": "Welcome to HT assessment",
            "Process": "populating all the pokemons into postgres"}
