#!/usr/bin/env python3
"""Define a function that takes a string & int or float and returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple containing k then the square of v

    Args:
        k (str): A string value to be added to the returned tuple.
        v (int or float): An int or float whose square val is also to be added.

    Returns:
        tuple: Of the string, and the square value of either the int or float.
    """

    return (k, v*v)
