#!/usr/bin/env python3
"""Annotate a func params and return values"""
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotated function
    """
    return [(i, len(i)) for i in lst]
