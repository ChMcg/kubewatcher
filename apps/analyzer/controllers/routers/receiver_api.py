from fastapi import APIRouter

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
        analyzed_data = AnalyzedData(analyzed_object)
        session.add(analyzed_data)
        session.refresh(analyzed_data)
        analyzed_metadata = AnalyzedMetadata(analyzed_object, analyzed_data)
        session.add(analyzed_metadata)
        session.commit()

    return {
        'severity': analyzed_object.severity, 
        'score': analyzed_object.severity_score
    }
