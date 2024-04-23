#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import List, Union


def element_length(lst: List[Union[int, str]]) -> List[int]:
    """Return a list of the lengths of the elements of lst."""
    return [len(i) for i in lst]
