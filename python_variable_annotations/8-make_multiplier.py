#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[Union[int, float]], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(n: Union[int, float]) -> float:
        """Multiply n by multiplier."""
        return n * multiplier
