#!/usr/bin/env python3
""" Module for aumming list of floats. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats list
    Args:
        input_list (List[float]): list of floats
    Returns:
        float: sum of floats
    """
    return sum(input_list)
