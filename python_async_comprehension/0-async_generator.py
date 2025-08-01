#!/usr/bin/env python3
''' generator '''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' list 0 to 10 and sleep 1'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
