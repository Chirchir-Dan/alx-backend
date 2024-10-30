#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class with a LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Adds an item to the cache using LIFO policy """
        if key is not None and item is not None:
            # If key already exists, remove it to update position
            if key in self.cache_data:
                self.order.remove(key)
            # Add item to cache and update order
            self.cache_data[key] = item
            self.order.append(key)

            # Check if we need to evict an item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Evict the most recently added item (LIFO)
                last_key = self.order.pop(-2)  # Second-last added key for LIFO
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        return self.cache_data.get(key, None)
