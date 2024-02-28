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

directory = '/Users/olivier/PycharmProjects/opdracht-2/raw'

# even tijdelijk
file_path = '/Users/olivier/PycharmProjects/opdracht-2/raw/customers.csv'

DB_PARAMS = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

schema_name = 'raw'
