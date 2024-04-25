#!/usr/bin/python3
"""This module defines a function that adds two float."""
import asyncio
from time import perf_counter
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    and return average time per task."""
    start_time = perf_counter()
    await wait_n(n, max_delay)
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
