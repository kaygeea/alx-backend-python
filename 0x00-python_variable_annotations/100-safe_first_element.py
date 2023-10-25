#!/usr/bin/env python3
"""Add type annotation for function with params of unknown type"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieve the first (i.e 0th) element of a sequence

    Arg(s):
        lst - Incoming argument for a sequence of vars of any type

    Return:
        The element at the 0th index of lst or None if lst is empty
    """
    if lst:
        return lst[0]
    else:
        return None
