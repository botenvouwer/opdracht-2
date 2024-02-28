import psycopg2
from constants import DB_PARAMS, table_names

source_schema = 'raw'
destination_schema = 'domain'

try:
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cursor:
            for table_name in table_names:
                sql = f'CREATE TABLE IF NOT EXISTS {destination_schema}.{table_name} AS SELECT * FROM {source_schema}.{table_name};'
                cursor.execute(sql)
                print(f'Table "{table_name}" transferred successfully.')

    print('All tables transferred successfully.')

except psycopg2.Error as e:
    print('Error:', e)
