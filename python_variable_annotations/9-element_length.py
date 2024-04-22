#!/usr/bin/env python3

from typing import Callable


"""
With the funtion's parameters :

    def element_length(lst):
    return [(i, len(i)) for i in lst]

Returns appropriate types
"""


def element_length(lst: list) -> list[tuple[any, int]]:
    """
    For the appropriate types we are :
    len the length of each element in the given list.
    lst the list of any type of elements.

    Returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
