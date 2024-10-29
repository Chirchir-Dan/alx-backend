#!/usr/bin/env python3
"""
Pagination module for managing and retrieving pages of a dataset.

This module defines a Server class that loads and paginates a dataset
of popular baby names. It includes a get_page method for retrieving a
specific page of data and a get_hyper method for retrieving pagination
metadata along with the dataset page. The index_range function is also
provided to calculate start and end indexes for a given page number
and page size.

Classes:
    Server: Loads and paginates a dataset of baby names.

Functions:
    index_range: Calculates start and end indexes for pagination.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """
     calculate the start and end indexes for a range of items.

     Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes for the page
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server instance with an empty dataset cache.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from a CSV file if not already loaded.

        Returns:
            List of list: The cached dataset, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset based on page no and size.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            list of list: The dataset page, or an empty list if the page
            is out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a dictionary with pagination details and data for a
        specific page.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing:
                - page_size: Length of the returned dataset page
                - page: The current page number
                - data: The dataset page (equivalent to get_page's return)
                - next_page: Number of the next page, None if no next page
                - prev_page: Number of the previous page, else None.
                - total_pages: The total number of pages in the dataset
        """
        # Get the requested page data
        data = self.get_page(page, page_size)

        # calculate total number of pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Construct the dictionary with pagination details
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
