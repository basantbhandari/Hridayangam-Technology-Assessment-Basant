import asyncio
import aiohttp


# Function to fetch all Pokémon asynchronously
async def fetch_all_pokemon(session) -> list:
    base_url = 'https://pokeapi.co/api/v2/pokemon'
    pokemon_list = []
    next_url = base_url

    while next_url:
        async with session.get(next_url) as response:
            data = await response.json()
            pokemon_list.extend(data['results'])
            next_url = data['next']

    return pokemon_list


# Function to fetch details of a specific Pokémon asynchronously
async def fetch_pokemon_details(session, url: str):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Error fetching details for {url}: {response.status}")
            return None


async def build_pokemons_items(pokemon_list: list) -> list[list]:
    result = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for pokemon in pokemon_list:
            tasks.append(fetch_pokemon_details(session, pokemon['url']))

        pokemon_details = await asyncio.gather(*tasks)

        for details in pokemon_details:
            if details:
                name = details['name']
                image_url = details['sprites']['other']['official-artwork']['front_default'] if \
                    details['sprites']['other']['official-artwork']['front_default'] else details['sprites'][
                    'front_default']
                types = ', '.join([type['type']['name'] for type in details['types']])
                abilities = ', '.join([ability['ability']['name'] for ability in details['abilities']])
                height = details['height']
                weight = details['weight']
                base_experience = details['base_experience']
                base_stats = details['stats']
                base_hp = next((stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'hp'), None)
                base_attack = next((stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'attack'),
                                   None)
                base_defense = next((stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'defense'),
                                    None)
                base_special_attack = next(
                    (stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'special-attack'), None)
                base_special_defense = next(
                    (stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'special-defense'), None)
                base_speed = next((stat['base_stat'] for stat in base_stats if stat['stat']['name'] == 'speed'),
                                  None)

                result.append([name, image_url, types, abilities, height, weight,
                               base_experience, base_hp, base_attack, base_defense,
                               base_special_attack, base_special_defense, base_speed])

    return result
