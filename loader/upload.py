from loader.reader import CSVReader
from model.entity import Header
import psycopg2
from psycopg2 import sql
from constants import DB_PARAMS, schema_name


class PostgresLoader:

    def __init__(self, db_params):
        self.db_params = db_params

    def load(self, reader: CSVReader):

        headers = reader.get_header_info()
        table_name = reader.get_name()

        with psycopg2.connect(**DB_PARAMS) as connection:
            with connection.cursor() as cursor:

                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")

                drop_if_exists = self.define_drop_if_exists_sql(schema_name, table_name)
                cursor.execute(drop_if_exists)
                create_table = self.define_create_table_sql(schema_name, table_name, headers)
                cursor.execute(create_table)
                connection.commit()

                for row in reader:
                    query = self.define_insert_sql(schema_name, table_name, headers, row)
                    insert_query = sql.SQL(query)

                    cursor.execute(insert_query, tuple(row))

                    connection.commit()

    def define_drop_if_exists_sql(self, schema_name: str, table_name: str):
        drop_if_exists_sql = sql.SQL("DROP TABLE IF EXISTS {}.{}").format(sql.Identifier(schema_name), sql.Identifier(table_name))
        return drop_if_exists_sql

    def define_create_table_sql(self, schema_name: str, table_name: str, headers: [Header]):
        column_info = self.define_column_info(headers)
        create_table_sql = sql.SQL("CREATE TABLE IF NOT EXISTS {}.{} ({})").format(sql.Identifier(schema_name), sql.Identifier(table_name), sql.SQL(column_info))
        return create_table_sql

    def define_column_info(self, header_list: [Header]):
        header_list_string = ', '.join(f"{header.name} {header.datatype}" for header in header_list)
        return header_list_string

    def define_insert_sql(self, schema_name: str, table_name: str, headers: [Header], values: []):
        header_names = ', '.join(f"{header.name}" for header in headers)

        query_head = f"INSERT INTO {schema_name}.{table_name} ({header_names}) "

        formatted_values = []

        for i, field in enumerate(values):
            datatype = headers[i].datatype
            if datatype == 'TEXT':
                formatted_values.append(f"'{field}'")
            else:
                formatted_values.append(field)

        query_body = f"VALUES ({', '.join(['%s' for _ in formatted_values])});"

        query = query_head + query_body
        return query
