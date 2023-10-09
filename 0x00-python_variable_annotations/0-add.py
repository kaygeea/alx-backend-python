#!/usr/bin/env python3
"""Defines a type-annotated function that sums 2 floats"""


def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers and return their sum.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of the two input numbers.
    """
    return float(a+b)
