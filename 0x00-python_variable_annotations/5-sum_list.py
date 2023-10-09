#!/usr/bin/env python3
"""Define a function that sums all the floating-point numbers in a list"""


def sum_list(input_list: [float]) -> float:
    """
    Add up all floating-point numbers in a list and return their sum.

    Args:
        input_list(list[float]): A list containing float values to be summed.

    Returns:
        float: the sum of all floating-point numbers in the input list.
    """
    sum_val: float = 0
    for val in input_list:
        sum_val += val
    return sum_val
