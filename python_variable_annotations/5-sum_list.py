#!/usr/bin/env python3

"Sum type float with an type-annotation sum_list wich take a list input_list"


def sum_list(input_list: list[float]) -> float:
    "Take type sum_list and returns the Sum type float"

    total = 0.0
    for num in input_list:
        total += num
    return total
