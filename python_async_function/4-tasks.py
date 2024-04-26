#!/usr/bin/env python3

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__("3-tasks").task_wait_random


"""
Take the code from 'wait_n' and alter for 'task_wait_n'
Import task_wait_random from 1-concurrent_coroutines.py file,
Create a measure_time function with integers n and max_delay for
to measures the total execution time for task_wait_n
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    Measures the total execution time for task_wait_n
    task_wait_random is called.
    Return the average time per iteration type float
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    return sorted(delays)
