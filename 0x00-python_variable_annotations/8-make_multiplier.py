#!/usr/bin/env python3
""" Module for Multiplication function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that return float multiplyied by a given multiplier
    Args:
        multiplier (float)
    Returns:
        Callable[[float], float]
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
