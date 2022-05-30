import json



class AnalyzedObject:
    original_object: dict
    severity: str
    severity_score: int

    def __init__(self, 
                original_audit_object: dict, 
                severity: str, 
                severity_score: int
            ) -> None:
        self.original_object = original_audit_object
        self.severity = severity
        self.severity_score = severity_score

    def dump(self) -> dict:
        return {
            "severity": {
                "level": self.severity,
                "score": self.severity_score,
            },
            "data": self.original_object
        }

    def dump_string(self) -> str:
        dumped_self = self.dump()
        return json.dumps(dumped_self, ensure_ascii=False)


