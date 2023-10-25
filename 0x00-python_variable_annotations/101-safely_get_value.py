#!/usr/bin/env python3
"""Define a type annotataed function"""
from typing import Any, Mapping, TypeVar, Union


def_type = TypeVar('T')
def_args = Union[def_type, None]
ret = Union[Any, def_type]


def safely_get_value(dct: Mapping, key: Any, default: def_args = None) -> ret:
    if key in dct:
        return dct[key]
    else:
        return default
