#!/usr/bin/env python3


"""
Take a String k with an type-annotation to_kv and a int or Float v wich
return a tuple.

k is the first element of tuple
v is a square of int or Float and is annoatated as a Float
"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    "Takes a string k and an int or Float v and returns a tuple"

    return k, float(v ** 2)