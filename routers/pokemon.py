from fastapi import APIRouter
from database.query import fetch_a_pokemon_by_name
from database.operations import execute_fetch_a_item_query
pokemon_router = APIRouter()


@pokemon_router.get('/pokemon/{name}')
async def get_pokemon_by_name(name: str):
    result = await execute_fetch_a_item_query(fetch_a_pokemon_by_name, name)
    return result
