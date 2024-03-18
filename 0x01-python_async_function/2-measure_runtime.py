#!/usr/bin/env python3
"""
Measure runtime
"""

import asyncio
from typing import List
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total excution rime for n times
    Args:
        n (int): number of times to call
        max_delay (int): Maximum delay
    Returns:
        float: Avarage run time for call
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
