#!/usr/bin/env python3
""" Module for tuple function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns tuple with string k and square of integer or float.
    Args;
        k (str): String
        v (int/float): integer or float
    Returns:
        Tuple[str, float]
    """
    return (k, v * v)
