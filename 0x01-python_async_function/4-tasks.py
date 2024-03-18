#!/usr/bin/env python3
"""
Tasks Module
"""

import asyncio
from typing import List
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous that spawns n times wait_random
    Args:
        n (int): Number of times to call
        max_delay (int): Maximum delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
