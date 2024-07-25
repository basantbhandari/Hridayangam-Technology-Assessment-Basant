from fastapi import APIRouter, Query
from database.operations import execute_fetch_by_params_query
pokemon_by_params_router = APIRouter()


@pokemon_by_params_router.get('/pokemon')
async def get_pokemon_by_params(name: str = Query(None), types: str = Query(None)):
    from database.query import fetch_pokemon_by_params_template
    query_params = []
    if name:
        fetch_pokemon_by_params_template += " AND name = $1"
        query_params.append(name)

    if types:
        types_list = types.split(',')
        fetch_pokemon_by_params_template += " AND types && ARRAY[" + ','.join(f"'{type_}'" for type_ in types_list) + "]"

    result = await execute_fetch_by_params_query(fetch_pokemon_by_params_template, query_params)
    return result
