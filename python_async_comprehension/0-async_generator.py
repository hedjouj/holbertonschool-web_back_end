#!/usr/bin/env python3
'''async generator'''

import asyncio, random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random(0, 10)
        