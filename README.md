# Hridayangam-Technology-Assessment-Basant

## Setup instructions
### Postgres setup instructions
    1. install Postgres server and pgadmin tool to query the database
    2. Create a brand new database eg. HT
    3. The created database creates a table named "pokemon_details" as
    ```
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

    4. verify the table one more time

### python setup instructions
    1. clone this repo and open the project in pycharm
    2. create local virtual environment as venv
    3. install requirements from requirements.txt
    '''
      pip install -r requirements. txt
    4. create the config.ini file in root dir(parallel to main.py) and update the content depending on your database settings as
    '''
    [DATABASE]
    DB_NAME = HT
    DB_USER = postgres
    DB_PASSWORD = root
    DB_HOST = localhost
    DB_PORT = 5432
    
    [MIS]
    API_PREFIX = /api/v1

    5. run main.py as 
      '''python main.py

    6. all details of Pokemons are fetched from "https://pokeapi.co/" place to Postgres table you have created when you visit "http://127.0.0.1:8080/". It will insert if not exit in the table else update the existing entry with a new entry
    7. using API client access the api's, according to the requirements
        1. home endpoint to load data from API to Postgres : "http://127.0.0.1:8080/"
        2. to see the name, types, and image_url for all the pokemons in Postgres table: "http://127.0.0.1:8080/api/v1/pokemons"
        3. api to get each pokemon from database by name in the url : "http://127.0.0.1:8080/api/v1/pokemon/kakuna"
        4. to filter using at least name or types or both api: "http://127.0.0.1:8080/api/v1/pokemon?name=charizard&types=fire,flying"



  ## All the code is in this repo, LMK if any confusion
    
