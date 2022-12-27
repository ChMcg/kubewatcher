import os

from models.database import PostgresConnectionModel


PostgresConnection = PostgresConnectionModel(
        os.getenv("POSTGRES_HOST"),
        int(os.getenv("POSTGRES_PORT")),
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASS"),
        os.getenv("POSTGRES_DATABASE"),
    )   
