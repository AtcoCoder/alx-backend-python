#!/usr/bin/env python3
"""1-async_comprehension module"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension()
    returns a list of ten random numbers
    """
    random_list = [random_num async for random_num in async_generator()]
    return random_list
