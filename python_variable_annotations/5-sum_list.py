#!/usr/bin/env python3

"Sum type Float with an type-annotation sum_list wich take a list input_list"


def sum_list(input_list: list[float]) -> float:
    "Take type sum_list and returns the Sum type Float"

    return sum(input_list)