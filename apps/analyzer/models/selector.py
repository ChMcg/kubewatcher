from __future__ import annotations

import json
import fnmatch
import re

from typing import Union
from models.severity import Severity, SeverityHelper, NotDefinedSeverity
from misc.exceptions import SelectorInnerMatchFailedException, \
    SubSelectorPathMissedException, \
    SeverityNotConfiguredExceprion


class SubSelector:
    selector: dict = {}
    severity: Severity

    def __init__(self, severity: Severity, selector: dict) -> None:
        self.severity = severity
        self.selector = selector

    def match(self, data: dict) -> bool:
        for path in self.selector.keys():
            try:
                resolved_data = self.resolve_object_as_str(path, data)
                selector_inner = self.selector[path]
                try:
                    if self.match_to_types(resolved_data, selector_inner):
                        return True
                except SelectorInnerMatchFailedException as e:
                    print(f"Error: {e} in selector_inner for path '{path}'")
            except SubSelectorPathMissedException:
                # Everything is fine, just data object doesn't have configured path
                continue
        return False

    def resolve_object_as_str(self, path: str, data: dict) -> str:
        obj = data
        for step in path.split('.'):
            try:
                obj = obj[step]
            except Exception:
                raise SubSelectorPathMissedException()
        return str(obj)

    def match_to_types(self, data: str, selector_inner: Union[str, dict]) -> bool:
        if isinstance(selector_inner, str): 
            return self.match_wildcard(data, selector_inner)

        elif isinstance(selector_inner, dict):
            if 'type' not in selector_inner.keys():
                print(f"Error field 'type' missing in selector_inner '{selector_inner}'")
                return False
            selector_type = selector_inner['type']
            if selector_type == 'regexp': return self.match_by_regexp(data, selector_inner)
            elif selector_type == 'set': return self.match_by_set(data, selector_inner)
        else:
            print(f"Error: unknown selector_inner: '{selector_inner}'")
            return False

    def match_wildcard(self, data: str, selector_inner: str) -> bool:
        return fnmatch.fnmatch(data, selector_inner)

    def match_by_set(self, data: str, selector_inner: dict) -> bool:
        if 'data' not in selector_inner.keys():
            print(f"Error: missing data in selector_inner '{selector_inner}'")
            return False
        target_set_list = selector_inner['data']
        if not isinstance(target_set_list, list):
            print(f"Error: selector_inner is not list '{selector_inner}'")
            return False
        target_set = set(target_set_list)
        return data in target_set

    def match_by_regexp(self, data: str, selector_inner: dict) -> bool:
        if 'data' not in selector_inner.keys():
            print(f"Error: missing data in selector_inner '{selector_inner}'")
            return False
        target_regexp = str(selector_inner['data'])
        return bool(re.match(target_regexp, data))


class Selector:
    selector: dict = {}
    sub_selectors: dict[str, SubSelector] = {}

    def __init__(self, selector_json_file: str) -> None:
        self.selector: dict = json.loads(open(selector_json_file, 'r').read())
        for name, value in self.selector.items():
            normalized_name = name
            try:
                normalized_name = SeverityHelper.resolve_severity_name(name)
            except SeverityNotConfiguredExceprion:
                new_severity = SeverityHelper.configure_new_severity(name)
                normalized_name = new_severity.fullname
            severity = SeverityHelper.get_severity_by_name(normalized_name)
            self.sub_selectors[normalized_name] = SubSelector(severity, value)

    def get_severity(self, audit_object: dict) -> tuple[str, int]:
        for level in SeverityHelper.get_severity_order():
            severity = SeverityHelper.get_severity_by_level(level)
            if severity.fullname in self.sub_selectors:
                sub_selector = self.sub_selectors[severity.fullname]
                if sub_selector.match(audit_object):
                    return sub_selector.severity.name, sub_selector.severity.score
        return NotDefinedSeverity().name, NotDefinedSeverity().score


if __name__ == '__main__':
    object_example = json.loads(open("logs/object_example_1.json", 'r').read())
    selector = Selector("configs/selector.json")
    severity = selector.get_severity(object_example)
    print(severity)
