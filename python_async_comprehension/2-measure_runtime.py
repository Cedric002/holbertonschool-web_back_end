#!/usr/bin/env python3

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
Import async_comprehension from 1-async_comprehension file,
Define `measure_runtime` a coroutine that execute in parallel
"""


async def measure_runtime():

    """
    With the help of coroutine measure_runtime, async_comprehension will
    execute async_comprehension four times in parallel using asyncio.gather
    measure_runtime return the measure the total runtime
    """

    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
