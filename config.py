import configparser

# Reading from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# get credentials
DB_NAME = config['DATABASE']["DB_NAME"]
DB_USER = config['DATABASE']["DB_USER"]
DB_PASSWORD = config['DATABASE']["DB_PASSWORD"]
DB_HOST = config['DATABASE']["DB_HOST"]
DB_PORT = config['DATABASE']["DB_PORT"]

API_PREFIX = config['MIS']["API_PREFIX"]
