#!/usr/bin/env python3

import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n

"""
Import wait_random from 1-concurrent_coroutines.py file,
Create a measure_time function with integers n and max_delay for
to measures the total execution time for wait_n
"""


def measure_time(n: int, max_delay: int) -> float:

    """
    Measures the total execution time for wait_n
    Return the average time per iteration type float
    """

    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
