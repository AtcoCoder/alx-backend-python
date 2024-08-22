#!/usr/bin/env python3
"""Function wait_n"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """ Wait spawn number of delays: n
    returns all the delays in a list
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
