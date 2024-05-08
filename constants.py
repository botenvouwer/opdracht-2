URLS = [
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/customers.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/employees.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/orders.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/productcategories.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/products.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/productsubcategories.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/vendorproduct.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/vendors.csv'
]

FILES = [url.split('/')[-1] for url in URLS]
TABLE_NAMES = [x.split('.')[0] for x in FILES]

# Directory where you want to download your files to and where they will be accessed when uploading
DIRECTORY = '/Users/olivier/PycharmProjects/opdracht-2/raw'

# Database parameters
DB_PARAMS_1 = {
    'host': 'data-olivier.postgres.database.azure.com',
    'port': '5432',
    'database': 'postgres',
    'user': 'pieter',
    'password': 'schieter=geen-mieter33'
}

DB_PARAMS = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

# Schema name for where you want to upload your files in the database
SCHEMA_NAME = 'raw'

CHUNK_SIZE = 70000
