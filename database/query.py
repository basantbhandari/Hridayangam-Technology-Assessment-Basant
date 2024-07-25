# SQL query with parameterized query
insert_and_update_pokemon_details_query = """
    INSERT INTO pokemon_details (name, image_url, types, abilities, height, weight,
                                base_experience, base_hp, base_attack, base_defense,
                                base_special_attack, base_special_defense, base_speed)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
    ON CONFLICT (name) DO UPDATE
    SET image_url = EXCLUDED.image_url,
        types = EXCLUDED.types,
        abilities = EXCLUDED.abilities,
        height = EXCLUDED.height,
        weight = EXCLUDED.weight,
        base_experience = EXCLUDED.base_experience,
        base_hp = EXCLUDED.base_hp,
        base_attack = EXCLUDED.base_attack,
        base_defense = EXCLUDED.base_defense,
        base_special_attack = EXCLUDED.base_special_attack,
        base_special_defense = EXCLUDED.base_special_defense,
        base_speed = EXCLUDED.base_speed
"""

fetch_all_pokemons = """
    SELECT name, image_url, types FROM pokemon_details;
"""

fetch_a_pokemon_by_name = """
    SELECT name, image_url, types FROM pokemon_details WHERE name = $1
"""

fetch_pokemon_by_params_template = """
    SELECT name, image_url, types FROM pokemon_details WHERE TRUE
"""