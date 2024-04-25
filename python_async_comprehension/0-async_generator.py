#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator

"""
Write a coroutine `async_generator` that takes no arguments
"""


async def async_generator() -> AsyncGenerator[float, None]:

    """
    Use a module `random` to loop the coroutine 10 times and
    give a random number between 0 and 10
    Asynchronous used for wait time for 1 second
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)