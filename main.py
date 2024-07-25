from fastapi import FastAPI
from config import API_PREFIX
from routers.pokemons import pokemons_router
from routers.pokemon import pokemon_router
from routers.pokemon_by_params import pokemon_by_params_router
from routers.home import home_router

app = FastAPI()

app.include_router(home_router)
app.include_router(pokemons_router, prefix=API_PREFIX)
app.include_router(pokemon_router, prefix=API_PREFIX)
app.include_router(pokemon_by_params_router, prefix=API_PREFIX)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8080)
