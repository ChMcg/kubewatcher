from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError

from controllers.analyzer import Analyzer
from database.postgres import Postgres
from models.orm import AnalyzedData, AnalyzedMetadata

router = APIRouter(
        prefix='/receiver',
        tags=['receiver'],
        dependencies=[]
    )

postgres = Postgres()


@router.put("/audit")
def receive_audit(data: dict) -> dict:
    analyzed_object = Analyzer.analyze(data)

    # store result in database 
    with postgres.session() as session:
        try:
            analyzed_data = AnalyzedData(analyzed_object)
            session.add(analyzed_data)
            session.flush()
            session.refresh(analyzed_data)
            analyzed_metadata = AnalyzedMetadata(analyzed_object, analyzed_data)
            session.add(analyzed_metadata)
            if "auditID" in analyzed_object.original_object:
                auditID = analyzed_object.original_object['auditID']
                print(f"Audit with id {auditID} added")
            session.commit()
        except SQLAlchemyError as e:
            print(f"Error occured: {e}")
            session.rollback()

    return {
        'severity': analyzed_object.severity, 
        'score': analyzed_object.severity_score
    }
