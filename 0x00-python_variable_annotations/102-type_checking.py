#!/usr/bin/env python3
""" Module to zoom in on element of tuple repeatdly function """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms the element of tuple by repeating based on the the factor
    Args:
        lst (Tuple): the input Tuple to be zoomed
        factor (int, Optional): the factor to repeach each element
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
