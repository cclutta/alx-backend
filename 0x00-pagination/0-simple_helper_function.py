#!/usr/bin/env python3
"""
Index range module

Contains the function index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing a start index and an end index.

    Args:
        page: the number of the page
        page_size: the size of the page
    """
    return (page_size * (page - 1), page_size * page)
