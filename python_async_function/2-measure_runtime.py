#!/usr/bin/env python3
"""This module defines a function that adds two float."""
import asyncio
from time import perf_counter
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function that returns the time"""
    first = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = perf_counter()
    total_time = finish - first
    return total_time / n
