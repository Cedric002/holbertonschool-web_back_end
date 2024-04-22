#!/usr/bin/env python3

from typing import Callable


"Take a float multiplier with an type-annotation make_multiplier"


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "Take type make_multiplier and returns the multiplier type Float"

    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
