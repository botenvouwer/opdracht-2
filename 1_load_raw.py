import os
from constants import DB_PARAMS, directory
from loader.reader import CSVReader
from loader.upload import PostgresLoader

# raw_files = os.listdir(directory)
#
# for filename in raw_files:
#     if filename.endswith('.csv'):
#         csv_path = os.path.join(directory, filename)
#         csv_reader = CSVReader(csv_path)
#         loader = PostgresLoader(DB_PARAMS)
#         loader.load(csv_reader)
#
#         from constants import DB_PARAMS
#         from loader.reader import CSVReader
#         from loader.upload import PostgresLoader

csv_4 = CSVReader('/Users/olivier/PycharmProjects/opdracht-2/raw/employees.csv')
loader = PostgresLoader(DB_PARAMS)
loader.load(csv_4)
