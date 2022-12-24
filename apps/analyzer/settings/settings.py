import os

from models.models import DBConnectionModel


# selector_file = os.getenv('SELECTOR_FILE') or 'selector.json'
# selector_file = os.getenv('SELECTOR_FILE') or 'configs/selector.json'
selector_file = os.getenv('SELECTOR_FILE') or '../../configs/selector.json'

# DBConnection = DBConnectionModel({
#     "user":     os.getenv('POSTGRES_USER') or "inelos",
#     "password": os.getenv('POSTGRES_PASS') or "r545TSvM",
#     "host":     os.getenv('POSTGRES_HOST') or "postgres",
#     "port":     os.getenv('POSTGRES_PORT') or "5432"
# })

DBConnection = DBConnectionModel({
        "user":     os.getenv('POSTGRES_USER') or "postgres",
        "password": os.getenv('POSTGRES_PASS') or "r545TSvM",
        "host":     os.getenv('POSTGRES_HOST') or "localhost",
        "port":     os.getenv('POSTGRES_PORT') or "5432"
    })

database_schema_file_path = os.getenv('DATABAS_SCHEMA_PATH') or 'schema.sql'
