from typing import Any


inc_holder = {}


def inc(context: Any, initial_value: int = 0) -> int:
    key = None
    if isinstance(context, type):
        key = context.__name__
    if isinstance(context, str):
        key = context
    if not key: raise Exception("Unknown context in `inc` function")

    if key not in inc_holder.keys():
        inc_holder[key] = initial_value
        return initial_value
    else:
        inc_holder[key] += 1
        return inc_holder[key]
