import psycopg2

from psycopg2.extensions import connection as pg_connection
from psycopg2.extensions import cursor as pg_cursor
from settings import DBConnection, database_schema_file_path


class DB:
    connection: pg_connection
    cursor: pg_cursor

    def __init__(self) -> None:
        self.connection = psycopg2.connect(
                user=DBConnection.user,
                password=DBConnection.password,
                host=DBConnection.host,
                port=DBConnection.port,
            )
        self.cursor = self.connection.cursor()
        if not self.check_if_all_tables_exists():
            self.create_default_schema()

    def exec_one(self, query: str) -> tuple:
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        # self.cursor.fetchall()
        return data
    
    def get_cursor(self) -> pg_cursor:
        return self.connection.cursor()

    def fetch_one(self) -> tuple:
        return self.cursor.fetchone()
    
    def commit(self):
        self.connection.commit()

    def check_if_all_tables_exists(self) -> bool:
        table_names = [
            'analyzed_data',
            'analyzed_metadata',
        ]
        schema = 'public'
        with self.connection.cursor() as cursor:
            for table_name in table_names:
                cursor.execute(f"select to_regclass('{schema}.{table_name}');")
                ret = cursor.fetchone()
                if len(ret) == 0 or ret[0] != table_name:
                    return False
        return True
    
    def create_default_schema(self):
        with self.connection.cursor() as cursor:
            cursor.execute(open(database_schema_file_path, 'r').read())
            self.connection.commit()
        

    

