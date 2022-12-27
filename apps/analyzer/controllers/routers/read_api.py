# import json
from fastapi import APIRouter

# from controllers.database import DB

router = APIRouter(
        prefix='/read',
        tags=['read'],
        dependencies=[]
    )

# db = DB()


# @router.get("/get_data_by_severity")
# def get_data_by_severity(severity: str) -> list[dict]:
#     data = []
#     with db.get_cursor() as cursor:
#         fields = ', '.join([
#             "am.severity",
#             "am.score",
#             "ad.object",
#         ])
#         cursor.execute(
#                 f"select {fields} from analyzed_data ad"
#                 f" inner join analyzed_metadata am "
#                 f" on ad.analyzed_data_id = am.analyzed_data_id"
#                 f" where am.severity = '{severity}'"
#             )
#         ret = cursor.fetchall()
#         for fetched_row in ret:
#             _, _, fetched_object = fetched_row
#             data.append(json.loads(fetched_object))
#     return data


# @router.get("/get_data_by_score_level")
# def get_data_by_score_level(treshold: int) -> list[dict]:
#     data = []
#     with db.get_cursor() as cursor:
#         fields = ', '.join([
#             "am.severity",
#             "am.score",
#             "ad.object",
#         ])
#         cursor.execute(
#                 f"select {fields} from analyzed_data ad"
#                 f" inner join analyzed_metadata am "
#                 f" on ad.analyzed_data_id = am.analyzed_data_id"
#                 f" where am.score > {treshold}"
#             )
#         ret = cursor.fetchall()
#         for fetched_row in ret:
#             _, _, fetched_object = fetched_row
#             data.append(json.loads(fetched_object))
#     return data
