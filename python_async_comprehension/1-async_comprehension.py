#!/usr/bin/env python3
""" async comprehension """
import asyncio
from typing import List, Vector
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector[float]:
    """ async comprehension """
    rnd = [i async for i in async_generator()]
    return rnd
