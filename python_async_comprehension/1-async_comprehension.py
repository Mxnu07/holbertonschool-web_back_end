#!/usr/bin/env python3
""" async comprehension """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """ async comprehension """
    rnd = [i async for i in async_generator()]
    return rnd
