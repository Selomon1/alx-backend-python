#!/usr/bin/env python3
"""
The module for basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and 10.
    Args:
        max_delay (int): Maximum delay
    Returns:
        float: random selected delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
