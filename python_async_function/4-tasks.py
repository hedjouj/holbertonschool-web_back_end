#!/usr/bin/env python3
'''tasks'''


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''wait random n times'''
    delays = [wait_random(max_delay) for _ in range(n)]
    delay: List[float] = await asyncio.gather(*delays)
    return sorted(delay)
