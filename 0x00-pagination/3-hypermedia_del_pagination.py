#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, accounting for deletions."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information that is resilient
        to deletions.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            dict: Dictionary with pagination information including:
                - 'index': Starting index for the current page.
                - 'next_index': Index to query for the next page.
                - 'page_size': The current page size.
                - 'data': The actual data for the current page.

        Raises:
            AssertionError: If index is out of range.
        """
        assert 0 <= index < len(self.indexed_dataset()), "Index out of range."

        data = []
        current_index = index
        dataset = self.indexed_dataset()

        # Collect page data
        while len(data) < page_size and current_index < len(dataset):
            item = dataset.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        # Next index to query based on current data position
        next_index = current_index if current_index < len(dataset) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
