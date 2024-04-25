#!/usr/bin/env python
"""This module defines a basic async function."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay time."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
