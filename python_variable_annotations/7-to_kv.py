#!/usr/bin/env python3

from typing import Tuple, Union

"""
Take a string k with an type-annotation to_kv and a int or float v wich
return a tuple.

k is the first element of tuple
v is a square of int or float and is annoatated as a float
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "Takes a string k and an int or float v and returns a tuple"

    return k, v ** 2
