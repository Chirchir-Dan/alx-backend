#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class with a FIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Adds an item to the cache using FIFO policy """
        if key is not None and item is not None:
            # If key already exists, remove it from the order list
            if key in self.cache_data:
                self.order.remove(key)
            # Add the item to the cache
            self.cache_data[key] = item
            self.order.append(key)

            # Check if we need to evict an item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Evict the first item in the order list (FIFO)
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        return self.cache_data.get(key, None)
