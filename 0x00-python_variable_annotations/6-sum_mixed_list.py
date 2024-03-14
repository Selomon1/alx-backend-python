#!/usr/bin/env python3
""" Module for summing mixed list function """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns sum of list (integers and floats)
    Args:
        mxd_list; list of integers and floats
    Return:
        float: the sum of the list
    """
    return sum(mxd_list)
