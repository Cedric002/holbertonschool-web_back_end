#!/usr/bin/env python3

import asyncio
from time import time
task_wait_n = __import__('2-measure_runtime').wait_n

"""
Take the code from 'wait_n' and alter for 'task_wait_n'
Import task_wait_random from 1-concurrent_coroutines.py file,
Create a measure_time function with integers n and max_delay for
to measures the total execution time for task_wait_n
"""


def task_wait_n(n: int, max_delay: int) -> float:
    
    """
    Measures the total execution time for task_wait_n
    task_wait_random is called.
    Return the average time per iteration type float
    """

    start_time = time()
    asyncio.run(task_wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
