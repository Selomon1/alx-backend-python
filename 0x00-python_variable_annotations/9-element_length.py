#!/usr/bin/env python3
""" Module for list of tuple function """

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuple conatin each element of list with its length
    """
    return [(i, len(i)) for i in lst]
