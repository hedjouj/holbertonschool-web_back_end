#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """function that return two int arg"""
    tuple = (page - 1) * page_size, page * page_size
    return tuple
