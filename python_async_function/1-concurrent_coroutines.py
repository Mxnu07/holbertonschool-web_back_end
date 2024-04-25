#!/usr/bin/env python3
"""This module defines a function that adds two float."""
from typing import List
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays."""
    lst = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(lst)]
    return finish
