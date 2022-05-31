from fastapi import APIRouter
from database import DB

from analyzer import Analyzer
from analyzed_object import AnalyzedObject

router = APIRouter(
        prefix='/receiver',
        tags=['receiver'],
        dependencies=[]
    )

db = DB()

@router.put("/audit")
def receive_audit(data: dict) -> dict:
    analyzed_object = Analyzer.analyze(data)
    # store result in database 
    with db.get_cursor() as cursor:
        cursor.execute(
                f"insert into analyzed_data"
                f" (object)"
                f" values ('{analyzed_object.dump_string()}')"
                f" returning analyzed_data_id"
            )
        inserted_id = cursor.fetchone()[0]
        print(f"AnalyzedObject with id {inserted_id} inserted")
        cursor.execute(
                f"insert into analyzed_metadata"
                f" (analyzed_data_id, severity, score)"
                f" values ('{inserted_id}', '{analyzed_object.severity}', '{analyzed_object.severity_score}')"
            )
        print(f"Metadata for AO {inserted_id} inserted")
        db.connection.commit()
    return {
        'severity': analyzed_object.severity, 
        'score': analyzed_object.severity_score
    }

