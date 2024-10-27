#!/usr/bin/env python3
"""
This function takes two integer arguments 'page' and 'page_size'. and returns a
tuple of size 2 containing a 'start_index' and and 'end_index' corresponding to
the range of indexes to return in a list for those particular pagination
parameters.
"""


def index_range(page: int, page_size: int) -> int:
    """
    returns index range
    """
    return (page_size * (page - 1), page_size * page)
