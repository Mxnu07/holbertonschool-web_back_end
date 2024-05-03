#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Type-annotated function index_range that takes a integer arguments. """
    return ((page - 1) * page_size, page * page_size)
