#!/usr/bin/env python3
"""Type checked using mypy"""

from typing import Union, Tuple, List


def zoom_array(lst: Tuple, factor: Union[int, float] = 2) -> List:
    """Zoom array returns list"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
