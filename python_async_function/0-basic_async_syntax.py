#!/usr/bin/env python3
''' wait '''


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''wait a random of time'''
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
