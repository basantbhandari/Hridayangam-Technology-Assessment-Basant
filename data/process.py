def build_all_pokemon_data(result: list[list]) -> list[tuple]:
    values = []
    for row in result:
        # Prepare data for insertion
        values.append((
            row[0],  # name
            row[1],  # image_url
            row[2].split(',') if row[2] else [],  # types (tuple)
            row[3].split(',') if row[3] else [],  # abilities (tuple)
            int(row[4]) if row[4] else None,  # height
            int(row[5]) if row[5] else None,  # weight
            int(row[6]) if row[6] else None,  # base_experience
            int(row[7]) if row[7] else None,  # base_hp
            int(row[8]) if row[8] else None,  # base_attack
            int(row[9]) if row[9] else None,  # base_defense
            int(row[10]) if row[10] else None,  # base_special_attack
            int(row[11]) if row[11] else None,  # base_special_defense
            int(row[12]) if row[12] else None  # base_speed
        ))
    return values
