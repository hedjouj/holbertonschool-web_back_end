#!/usr/bin/env python3
"""Module that defines an asynchronous comprehension function."""

from typing import List
from ('0-async_generator') __import__ async_generator  # if this doesn't work use the form below:
from 0-.async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers asynchronously from async_generator."""
    return [i async for i in async_generator()]
