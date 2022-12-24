from enum import IntEnum
from misc.exceptions import SeverityNotConfiguredExceprion
from misc.enum_helper import inc


class SeverityLevels(IntEnum):
    critical    = 4
    warning     = 3
    info        = 2
    metadata    = 1
    not_defined = 0


class Severity:
    level: int
    name: str
    score: int
    fullname: str

    def __init__(self, level: int, name: str, score: int) -> None:
        self.level = level
        self.fullname = name if ':' in name else f"{name}:{level}"
        self.name = name.split(':')[0]
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
    configured = dict([ (x.score, x) for x in all_severeties() ])
    severity_by_names = dict([ (x.fullname, x) for x in all_severeties() ])

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
        levels = sorted(SeverityHelper.configured.keys())[::-1]
        return levels

    @staticmethod
    def resolve_severity_name(name: str) -> str:
        for severity in all_severeties():
            if severity.name.lower() == name.lower():
                return severity.fullname
        raise SeverityNotConfiguredExceprion()

    @staticmethod
    def configure_new_severity(name: str) -> Severity:
        new_severity_name = name
        score: int
        if ':' in name:
            a, b = name.split(':')
            new_severity_name, score = a, int(b)
        else:
            score = inc(SeverityHelper, SeverityLevels.critical)

        new_severity = Severity(score, new_severity_name, score)
        SeverityHelper.configured[score] = new_severity
        SeverityHelper.severity_by_names[name] = new_severity
        return new_severity
