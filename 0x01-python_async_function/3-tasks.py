#!/usr/bin/env python3
"""task_wait_random function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ task_wait_random(max_delay)
    return a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
