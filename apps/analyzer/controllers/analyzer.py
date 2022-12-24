from controllers.database import DB
from models.analyzed_object import AnalyzedObject
from models.selector import Selector
from settings.settings import selector_file

db = DB()
selector = Selector(selector_file)


class Analyzer:

    @staticmethod
    def analyze(data: dict):
        # data_parsed = json.loads(data)
        data_parsed = data
        severity, score = selector.get_severity(data_parsed)
        return AnalyzedObject(data_parsed, severity, score)
