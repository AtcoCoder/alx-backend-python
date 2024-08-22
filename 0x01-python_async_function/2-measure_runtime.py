#!/usr/bin/env python3
"""Function measure_time"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure_time(n: int, max_delay: int)

    returns the total time taken to complete executing
     the wait_n function: total_time / n
     n: number of delays to th wait_n function
     max_delay: maximum period of delay passed into the wait_n function
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
