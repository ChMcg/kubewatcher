from models.analyzed_object import AnalyzedObject
from models.selector import Selector
from settings.settings import selector_file

selector = Selector(selector_file)


class Analyzer:

    @staticmethod
    def analyze(data: dict) -> AnalyzedObject:
        data_parsed = data
        severity, score = selector.get_severity(data_parsed)
        return AnalyzedObject(data_parsed, severity, score)
