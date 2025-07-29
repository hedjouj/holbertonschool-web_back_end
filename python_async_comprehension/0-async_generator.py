#!/usr/bin/env python3
'''async generator'''


import asyncio
import random
from typing import async_generator


async def async_generator() -> async_generator[float, None]:
    '''async genrator'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
