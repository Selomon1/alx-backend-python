#!/usr/bin/env python3
"""
Async Comprehension
"""

from typing import List
from asyncio import gather
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async comprehension to collect 10 random numbers """
    return [i async for i in async_generator()]
