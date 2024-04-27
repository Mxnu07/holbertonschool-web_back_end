#!/usr/bin/env python3
""" async comprehension """
from typing import List
from typing import Union

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Union[float, int]]:
    """ async comprehension """
    rnd = [float(i) async for i in async_generator()]
    return rnd
