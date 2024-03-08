import os
from constants import DB_PARAMS, directory
from loader.reader import CSVReader
from loader.upload import PostgresLoader
from loader.download import Download

# # Stap 1 download de files (via loader.download.py)
dlf = Download()
dlf.download_files()

# Stap 2 upload de files naar het raw schema van de database (via loader.upload.py)
ulf = PostgresLoader(DB_PARAMS)

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print(f"Loading {filename}")
        filepath = os.path.join(directory, filename)
        csv = CSVReader(filepath)
        ulf.load(csv)
        print(f"Succesfully loaded {filename}")
