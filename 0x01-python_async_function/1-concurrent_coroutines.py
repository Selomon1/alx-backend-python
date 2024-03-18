#!/usr/bin/env python3
"""
Concurrent coroutines module
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    Args:
        n (int): Number of times to call wait-random.
        max_delay (int): Maximum delay.
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
