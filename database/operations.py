import asyncpg
import config


async def insert_or_update_data(query: str, data: list[tuple]) -> None:
    """ Insert data into Postgres SQL table """
    conn = await asyncpg.connect(user=config.DB_USER,
                                 password=config.DB_PASSWORD,
                                 database=config.DB_NAME,
                                 host=config.DB_HOST,
                                 port=config.DB_PORT)
    try:
        await conn.executemany(query, data)
        print("Data inserted successfully!")

    except asyncpg.PostgresError as e:
        print(f"Error inserting data: {e}")
    finally:
        await conn.close()
        print("Postgres SQL connection closed")


async def execute_fetch_query(query: str) -> list:
    conn = await asyncpg.connect(user=config.DB_USER,
                                 password=config.DB_PASSWORD,
                                 database=config.DB_NAME,
                                 host=config.DB_HOST,
                                 port=config.DB_PORT)
    try:
        result = await conn.fetch(query)
        # Convert the result to a list of dictionaries
        rows = []
        for record in result:
            # Convert the record to a dictionary
            row = {key: (str(value) if not isinstance(value, list) else value) for key, value in dict(record).items()}
            rows.append(row)
        return rows
    except asyncpg.PostgresError as e:
        print(f"Error inserting data: {e}")
    finally:
        await conn.close()
        print("Postgres SQL connection closed")


async def execute_fetch_a_item_query(query: str, name: str) -> dict:
    conn = await asyncpg.connect(user=config.DB_USER,
                                 password=config.DB_PASSWORD,
                                 database=config.DB_NAME,
                                 host=config.DB_HOST,
                                 port=config.DB_PORT)
    try:
        result = await conn.fetchrow(query, name)
        # Convert the result to a dictionary with string values
        row = {key: (str(value) if not isinstance(value, list) else value) for key, value in dict(result).items()}
        return row

    except asyncpg.PostgresError as e:
        print(f"Error inserting data: {e}")
    finally:
        await conn.close()
        print("Postgres SQL connection closed")


async def execute_fetch_by_params_query(query: str, params: list) -> list:
    conn = await asyncpg.connect(user=config.DB_USER,
                                 password=config.DB_PASSWORD,
                                 database=config.DB_NAME,
                                 host=config.DB_HOST,
                                 port=config.DB_PORT)
    try:
        result = await conn.fetch(query, *params)
        # Convert the result to a list of dictionaries
        return [{key: (str(value) if not isinstance(value, list) else value) for key, value in dict(record).items()} for
                record in result]

    except asyncpg.PostgresError as e:
        print(f"Error inserting data: {e}")
    finally:
        await conn.close()
        print("Postgres SQL connection closed")
