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
                    query = self.define_insert_sql(schema_name, table_name, headers)

                    cursor.execute(query, tuple(row))

                    connection.commit()

    def define_drop_if_exists_sql(self, schema_name: str, table_name: str):
        drop_if_exists_sql = sql.SQL("DROP TABLE IF EXISTS {}.{}").format(sql.Identifier(schema_name), sql.Identifier(table_name))
        return drop_if_exists_sql

    def define_create_table_sql(self, schema_name: str, table_name: str, headers: [Header]):
        column_info = self.define_column_info(headers)
        create_table_sql = sql.SQL("CREATE TABLE IF NOT EXISTS {}.{} ({})").format(sql.Identifier(schema_name), sql.Identifier(table_name), column_info)
        return create_table_sql

    def define_column_info(self, header_list: [Header]):
        header_list_string = []
        for header in header_list:
            # string manipulatie van camelcase naar snakecase
            header_list_string.append(sql.SQL("{} {}").format(sql.Identifier(header.name), sql.SQL(header.datatype)))

        header_list_string = sql.SQL(', ').join(header_list_string)

        return header_list_string

    def define_insert_sql(self, schema_name: str, table_name: str, headers: [Header]):
        header_names = []
        for header in headers:
            header_names.append(sql.SQL("{}").format(sql.Identifier(header.name)))

        header_names = sql.SQL(', ').join(header_names)

        query_head = sql.SQL("INSERT INTO {}.{} ({})").format(sql.Identifier(schema_name), sql.Identifier(table_name), header_names)
        query_body = sql.SQL("VALUES ({});").format(
            sql.SQL(', '.join(['%s'] * len(headers))))
#         query_body = f"VALUES ({', '.join(['%s'] * len(headers))});"

        query = query_head + query_body
        return query
