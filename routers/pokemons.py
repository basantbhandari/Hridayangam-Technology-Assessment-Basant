from fastapi import APIRouter
from database.query import fetch_all_pokemons
from database.operations import execute_fetch_query
pokemons_router = APIRouter()


@pokemons_router.get('/pokemons')
async def get_pokemons():
    result = await execute_fetch_query(fetch_all_pokemons)
    return result
