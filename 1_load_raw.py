import os
from constants import DB_PARAMS, DIRECTORY, SCHEMA_NAME, FILES, URLS, CHUNK_SIZE, DB_PARAMS_1
from loader.reader import CSVReader
from loader.upload import PostgresLoader
from loader.download import Download

# # Stap 1 download de files (via loader.download.py)
dlf = Download(URLS, DIRECTORY)
dlf.download_files()

# Stap 2 upload de files naar het raw schema van de database (via loader.upload.py)
ulf = PostgresLoader(DB_PARAMS, SCHEMA_NAME, CHUNK_SIZE)

print(f"The used chunk size is {ulf.chunk_size}")
for filename in os.listdir(DIRECTORY):
    if filename in FILES:
        if filename.endswith(".csv"):
            print(f"Loading {filename}")
            filepath = os.path.join(DIRECTORY, filename)
            csv = CSVReader(filepath)
            ulf.load(csv)
            print(f"Succesfully loaded {filename}")
