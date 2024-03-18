#!/usr/bin/env python3
"""
Task module
"""

import asyncio
from typing import List
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Function that takes integer max_delay and returns an asyncio.Task obmject
    Args:
        max_delay (int): Maximum delay
    """
    return asyncio.create_task(wait_random(max_delay))
