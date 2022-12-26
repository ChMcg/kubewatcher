import json
from sqlalchemy.exc import SQLAlchemyError

from database.postgres import Postgres
from models.base_model import BaseSqlModel
from controllers.analyzer import Analyzer
from models.orm import AnalyzedData, AnalyzedMetadata


class TestDatabaseInteraction():

    def test_postres_connection(self):
        postgres = Postgres()
        engine = postgres.engine
        metadata = BaseSqlModel.metadata
        metadata.reflect(engine)
        print(metadata.tables.keys())

    def test_object_write_to_database(self):
        postgres = Postgres()
        with postgres.session() as session:
            try:
                # parse object example
                with open("examples/object_example_1.json", 'r') as object_example:
                    object_example = json.load(object_example)
                local_analyzed_obj = Analyzer.analyze(object_example)
                # add parsed data to database
                data = AnalyzedData(local_analyzed_obj)
                session.add(data)
                session.flush()
                session.refresh(data)
                print(f'data.analyzed_data_id: {data.analyzed_data_id}')
                metadata = AnalyzedMetadata(local_analyzed_obj, data)
                session.add(metadata)
                session.commit()
                # and then delete created records
                session.delete(metadata)
                session.flush()
                session.delete(data)
                session.commit()
            except SQLAlchemyError:
                session.rollback()
                raise
