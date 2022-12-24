import sqlalchemy
from sqlalchemy.orm import Session

from settings.app import PostgresConnection


class Postgres():
    engine: sqlalchemy.Engine

    def __init__(self) -> None:
        self.engine = sqlalchemy.create_engine(
                PostgresConnection.to_sqlachemy_connection_string()
            )   

    def session(self) -> Session:
        return Session(self.engine)
