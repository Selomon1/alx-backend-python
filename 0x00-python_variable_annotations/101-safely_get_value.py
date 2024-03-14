#!/usr/bin/env python3
""" Module for safely retrieving values from dictionaries. """

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves value from dictionary, given a key
    Args:
        dct (Mapping): dictionary to retrieve the value
        key (Any): Key to look up
        default (Union[T, None], optional): default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
