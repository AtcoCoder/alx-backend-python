#!/usr/bin/env python3
"""2-measure_runtime module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtion()
    return the total time taken to execute the
    async_comprehension coroutine four times
    """
    start = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    result = await asyncio.gather(*tasks)
    end = time.perf_counter()
    total_time = end - start
    return total_time
