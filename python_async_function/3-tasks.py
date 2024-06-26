#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

"""
Import wait_random from 0-basic_async_syntax.py file,
Not use an async function but a regular function syntax
"""


def task_wait_random(max_delay: int) -> asyncio.Task:

    """
    Define task_wait_random that takes an integer max_delay
    Returns a asyncio.Task
    """

    coroutine = wait_random(max_delay)

    task = asyncio.create_task(coroutine)

    return task
