#!/usr/bin/env python3
"""Define a function that sums all the values in a list of mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Add up all the nums in a list of mixed variable types and return their sum.

    Args:
        mxd_lst([int | float]): A list of int & float values to be summed.

    Returns:
        float: the sum of all values in the input list.
    """
    sum_mixed_vals: float = 0

    for mixed_var_val in mxd_lst:
        sum_mixed_vals += mixed_var_val
    return sum_mixed_vals
