#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Sum a list of floats and integers."""
    return sum(mxd_lst)
