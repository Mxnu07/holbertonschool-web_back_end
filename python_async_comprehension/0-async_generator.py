#!/usr/bin/env python3
""" async generator """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ async generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
