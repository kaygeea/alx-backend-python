#!/usr/bin/env python3
"""Create a function that takes a float and returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a multiplier function.

    Args:
        multiplier(float): A float value to be used as a multiplier

    Returns:
        Callable[[float], float]: A function that takes a float and returns the
        result of multiplying it by 'multiplier'.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply a float by 'multiplier'.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
