from enum import IntEnum
from exceptions import SeverityNotConfiguredExceprion
from enum_helper import inc



class SeverityLevels(IntEnum):
    critical    = 1
    warning     = 2
    info        = 3
    metadata    = 4
    not_defined = 1000


class Severity:
    level: int
    name: str
    score: int

    def __init__(self, level: int, name: str, score: int) -> None:
        self.level = level
        self.name = name
        self.score = score


class CriticalSeverity(Severity):
    def __init__(self) -> None:
        super().__init__(SeverityLevels.critical, "Critical", 100)

        
class WarningSeverity(Severity):
    def __init__(self) -> None:
        super().__init__(SeverityLevels.warning, "Warning", 75)


class InfoSeverity(Severity):
    def __init__(self) -> None:
        super().__init__(SeverityLevels.info, "Info", 25)


class MetadataSeverity(Severity):
    def __init__(self) -> None:
        super().__init__(SeverityLevels.metadata, "Metadata", 10)


class NotDefinedSeverity(Severity):
    def __init__(self) -> None:
        super().__init__(SeverityLevels.not_defined, "NotDefined", 5)


def all_severeties() -> list[Severity]:
    return [
            CriticalSeverity(),
            WarningSeverity(),
            InfoSeverity(),
            MetadataSeverity(),
            NotDefinedSeverity(),
        ]


class SeverityHelper:
    configured = dict([ (x.level, x) for x in all_severeties() ])
    severity_by_names = dict([ (x.name, x) for x in all_severeties() ])

    @staticmethod
    def get_severity_by_name(severity_name: str) -> Severity:
        if severity_name in SeverityHelper.severity_by_names.keys():
            return SeverityHelper.severity_by_names[severity_name]
        else:
            new_severity = SeverityHelper.configure_new_severity(severity_name)
            return new_severity
        
    @staticmethod
    def get_severity_by_level(level: int) -> Severity:
        return SeverityHelper.configured[level]

    @staticmethod
    def get_severity_order() -> list[int]:
        levels = sorted(SeverityHelper.configured.keys())
        return levels

    @staticmethod
    def resolve_severity_name(name: str) -> str:
        for severity in all_severeties():
            if severity.name.lower() == name.lower():
                return severity.name
        raise SeverityNotConfiguredExceprion()
        
    @staticmethod
    def configure_new_severity(name: str) -> Severity:
        new_severity_level = inc(SeverityHelper, SeverityLevels.metadata)
        new_severity = Severity(new_severity_level, name)
        SeverityHelper.configured[new_severity_level] = new_severity
        SeverityHelper.severity_by_names[name] = new_severity
        return new_severity
