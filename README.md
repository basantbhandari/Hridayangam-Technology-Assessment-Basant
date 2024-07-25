
# Hridayangam-Technology-Assessment-Basant

## Setup Instructions

### PostgreSQL Setup Instructions

1. Install PostgreSQL server and pgAdmin tool to query the database.
2. Create a brand new database, e.g., `HT`.
3. Create a table named `pokemon_details` in the created database using the following SQL:
    ```sql
    -- Table: public.pokemon_details
    -- DROP TABLE IF EXISTS public.pokemon_details;

    CREATE TABLE IF NOT EXISTS public.pokemon_details
    (
        name character varying(100) COLLATE pg_catalog."default" NOT NULL,
        image_url text COLLATE pg_catalog."default",
        types text[] COLLATE pg_catalog."default",
        abilities text[] COLLATE pg_catalog."default",
        height integer,
        weight integer,
        base_experience integer,
        base_hp integer,
        base_attack integer,
        base_defense integer,
        base_special_attack integer,
        base_special_defense integer,
        base_speed integer,
        CONSTRAINT pokemon_details_pkey PRIMARY KEY (name)
    )
    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.pokemon_details
        OWNER to postgres;
    ```
4. Verify the table creation.

### Python Setup Instructions

1. Clone this repository and open the project in PyCharm.
2. Create a local virtual environment (venv).
3. Install the required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `config.ini` file in the root directory (parallel to `main.py`) and update the content according to your database settings:
    ```ini
    [DATABASE]
    DB_NAME = HT
    DB_USER = postgres
    DB_PASSWORD = root
    DB_HOST = localhost
    DB_PORT = 5432
    
    [MIS]
    API_PREFIX = /api/v1
    ```
5. Run `main.py`:
    ```bash
    python main.py
    ```
6. All Pokémon details are fetched from [PokeAPI](https://pokeapi.co/) and inserted into the PostgreSQL table when you visit `http://127.0.0.1:8080/`. If a Pokémon already exists, its entry is updated.
7. Use an API client to access the APIs as per the requirements:
    1. Home endpoint to load data from API to PostgreSQL: `http://127.0.0.1:8080/`
    2. To see the name, types, and image_url for all the Pokémon in the PostgreSQL table: `http://127.0.0.1:8080/api/v1/pokemons`
    3. API to get each Pokémon from the database by name in the URL: `http://127.0.0.1:8080/api/v1/pokemon/kakuna`
    4. To filter using at least name or types or both: `http://127.0.0.1:8080/api/v1/pokemon?name=charizard&types=fire,flying`

---

## All the code is in this repo. Let me know if there is any confusion.
