#!/usr/bin/env python3
"""
This module has two methods named get_page and get_index that we wrote above.
get page takes two integer arguments page with default value of 1 and
page_size with a default value 10.
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """
    returns index range
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        This is a constructor for the class
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes in two integers page and page_size with default values 1 and 10.
        uses assert to verify that both integers are greater than 0
        uses index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset (i.e correct
        list of rows).
        returns empty list is input arguments are out of range for the dataset.
        """

        # Verify both args are ints and > 0
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(
            page_size, int
            ) and page_size > 0, "Page size must be a positive integer"

        # Calculate index range
        start, end = index_range(page, page_size)

        # Fetch dataset and slice the desired page
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]
