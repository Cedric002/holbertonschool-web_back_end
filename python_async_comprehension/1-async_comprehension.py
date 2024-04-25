#!/usr/bin/env python3

async_generator = __import__('0-async_generator').async_generator

"""
Import async_generator from 0-async_generator file,
Define `async_comprehension` a coroutine that takes no arguments
"""


async def async_comprehension():

    """
    With the help of coroutine async_generator, async_comprehension will
    generate 10 random numbers and returns them async
    """

    return [num async for num in async_generator()]
