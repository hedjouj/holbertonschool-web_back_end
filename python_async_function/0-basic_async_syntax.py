#!/usr/bin/env python3
'''The basics of async'''


import asyncio, random


async def max_delay(int = 10):
    '''async function syntax'''
    await asyncio.sleep(0, max_delay)
    return max_delay(float)
