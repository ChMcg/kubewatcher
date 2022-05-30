import json

from database import DB
from selector import Selector
from settings import selector_file
from analyzed_object import AnalyzedObject

db = DB()
selector = Selector(selector_file)

class Analyzer:
    pass

    @staticmethod
    def analyze(data: dict):
        # data_parsed = json.loads(data)
        data_parsed = data
        severity, score = selector.get_severity(data_parsed)
        return AnalyzedObject(data_parsed, severity, score)
