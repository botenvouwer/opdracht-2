urls = [
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/customers.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/employees.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/orders.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/productcategories.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/products.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/productsubcategories.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/vendorproduct.csv',
    'https://raw.githubusercontent.com/sfrechette/adventureworks-neo4j/master/data/vendors.csv'
]

files = [url.split('/')[-1] for url in urls]
table_names = [x.split('.')[0] for x in files]

# Directory where you want to download your files to and where they will be accessed when uploading
directory = '/Users/olivier/PycharmProjects/opdracht-2/raw'

# Database parameters
DB_PARAMS = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

# Schema name for where you want to upload your files in the database
schema_name = 'raw'
