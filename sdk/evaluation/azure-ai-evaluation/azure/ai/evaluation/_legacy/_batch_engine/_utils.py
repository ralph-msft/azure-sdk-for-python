# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import inspect
import os
import re
from typing import Any, Final, Mapping, Sequence, Tuple


DEFAULTS_KEY: Final[str] = "$defaults$"


def normalize_identifier_name(name: str) -> str:
    """Normalize the identifier name to a valid Python variable name.

    Args:
        name (str): The identifier name to normalize.

    Returns:
        str: The normalized identifier name.
    """
    normalized = re.sub(r"\W", "_", name.strip())
    if normalized[0].isdigit():
        normalized = f"_{normalized}"
    return normalized


def get_value_from_path(path: str, data: Mapping[str, Any]) -> Tuple[bool, Any]:
    """Tried to get a value from a mapping based on the specified path. The path is a
    string with dot-separated keys (e.g. data.nested_1.nested_2).

    This will interpret the path prioritizing a depth first search with the shortest
    key possible at each level. If for example you had the following data:
    {
        "foo": {
            "bar": {
                "happy": 12
            }
        },
        "foo.bar": {
            "none": 14,
            "random": { "some": 15 }
        },
        "foo.bar.none": 16
    }
    And you asked for foo.bar.none, the returned value would be 14"
    """

    def _get_value(data: Mapping[str, Any], parts: Sequence[str]) -> Tuple[bool, Any]:
        if len(parts) == 0:
            return True, data

        for i in range(1, len(parts) + 1):
            key = ".".join(parts[:i])
            if isinstance(data, Mapping) and key in data:
                found, match = _get_value(data[key], parts[i:])
                if found:
                    return found, match

        return False, None

    if path is None or data is None:
        return False, None

    parts = path.strip().split(".")
    if len(parts) == 0:
        return False, None
    return _get_value(data, parts)


def is_async_callable(obj: Any) -> bool:
    """Check if the object is an async callable. This will be true if the object is a coroutine function,
    or if the object has

    :param Any obj: The object to check.
    :return: True if the object is an async callable.
    :rtype: bool
    """
    return (
        inspect.iscoroutinefunction(obj)
        or inspect.iscoroutinefunction(getattr(obj, "__call__", None))
    )
