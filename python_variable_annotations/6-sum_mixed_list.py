#!/usr/bin/env python3

from typing import List, Union

"Sum type Float with an type-annotation sum_mixed_list wich take a list mxd_lst"


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "Take type sum_mixed_list and returns the Sum type Float"

    return sum(mxd_lst)