#!/usr/bin/env python3

import asyncio
import random

"Define wait_random that waits for a random delay between 0 and max_delay"


async def wait_random(max_delay: int = 10) -> float:

    """
    Random delay between 0 and max_delay.

    max_delay is a maximum delay type float in seconds, defaults to 10.

    Returns the actual delay type float in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
