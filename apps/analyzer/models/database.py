from dataclasses import dataclass


@dataclass
class PostgresConnectionModel:
    host: str 
    port: int 
    user: str 
    password: str 
    database: str = 'analyzer'

    def to_psycopg2_connection_string(self) -> str:
        # TODO
        raise NotImplementedError()

    def to_sqlachemy_connection_string(self) -> str:
        """ 
        Create SQLAlchemy connection string in format:
        `postgresql+psycopg2://user:password@host:port/dbname`

        see: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#dialect-postgresql-psycopg2-connect
        """
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
