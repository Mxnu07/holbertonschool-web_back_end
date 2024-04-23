#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    Returns a tuple with the first element as
    the input key and the second element as
    the square of the input value.
    """
    return (k, (v**2))
