#!/usr/bin/env python3

import asyncio
from basic_async_syntax import wait_random # type: ignore
from typing import List

"""
Import wait_random from 0-basic_async_syntax.py file,
Spawn wait_random n times with the specified max_delay.
"""


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    Spawns `wait_random` n times

    Returns the list of delays in ascending order
    without using sort() because of concurrency.
    """

    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
