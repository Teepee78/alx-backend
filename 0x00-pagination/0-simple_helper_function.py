#!/usr/bin/env python3
"""
Defines index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: Tuple containing the start and end indexes
    """

    start = (page - 1) * page_size
    return (start, start + page_size)
