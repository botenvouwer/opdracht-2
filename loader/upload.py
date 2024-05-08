from psycopg2.extras import execute_values
from loader.reader import CSVReader
from model.entity import Header
import psycopg2
from psycopg2 import sql
import re


class PostgresLoader:

    def __init__(self, db_params, schema_name, chunk_size=50):
        self.db_params = db_params
        self.schema_name = schema_name
        self.chunk_size = chunk_size

    def load(self, reader: CSVReader):

        headers = reader.get_header_info()
        table_name = reader.get_name()

        with psycopg2.connect(**self.db_params) as connection:
            with connection.cursor() as cursor:

                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")

                drop_if_exists = self.define_drop_if_exists_sql(self.schema_name, table_name)
                cursor.execute(drop_if_exists)
                create_table = self.define_create_table_sql(self.schema_name, table_name, headers)
                cursor.execute(create_table)
                connection.commit()

                csv_iter = iter(reader)
                query = self.define_insert_sql(self.schema_name, table_name, headers)
                while True:
                    chunk = self.chunk_maker(csv_iter)
                    if len(chunk)==0:
                        break
                    else:
                        execute_values(cursor, query, chunk)

                connection.commit()

    def define_drop_if_exists_sql(self, schema_name: str, table_name: str):
        drop_if_exists_sql = sql.SQL("DROP TABLE IF EXISTS {}.{}").format(sql.Identifier(schema_name), sql.Identifier(table_name))
        return drop_if_exists_sql

    def define_create_table_sql(self, schema_name: str, table_name: str, headers: [Header]):
        for header in headers:
            header.name = self.camel_to_snake(header.name)
        column_info = self.define_column_info(headers)
        create_table_sql = sql.SQL("CREATE TABLE IF NOT EXISTS {}.{} ({})").format(sql.Identifier(schema_name), sql.Identifier(table_name), column_info)
        return create_table_sql

    def define_column_info(self, header_list: [Header]):
        header_list_string = []
        for header in header_list:
            snake_case_name = self.camel_to_snake(header.name)
            header_list_string.append(sql.SQL("{} {}").format(sql.Identifier(snake_case_name), sql.SQL(header.datatype)))

        header_list_string = sql.SQL(', ').join(header_list_string)

        return header_list_string

    def define_insert_sql(self, schema_name: str, table_name: str, headers: [Header]):
        header_names = []
        for header in headers:
            snake_case_name = self.camel_to_snake(header.name)
            header_names.append(sql.SQL("{}").format(sql.Identifier(snake_case_name)))

        header_names = sql.SQL(', ').join(header_names)

        query = sql.SQL("INSERT INTO {}.{} ({}) VALUES %s").format(sql.Identifier(schema_name), sql.Identifier(table_name), header_names)

        return query

    def camel_to_snake(self, camel_name: str):
        camel_name_2 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_name)
        snake_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_name_2).lower()
        return snake_name

    def chunk_maker(self, csv: iter):
        # voor elke keer dat de functie wordt aangeroepen wordt de header-regel en eerstvolgende chunk returned
        chunk = []

        # voeg de volgende regel toe aan de chunk.
        for x in range(self.chunk_size):
            try:
                if len(chunk) < self.chunk_size:
                    next_row = next(csv)
                    chunk += [next_row]

            except StopIteration:
                break

        return chunk
