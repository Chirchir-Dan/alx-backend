#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class with a LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Adds an item to the cache using LIFO policy """
        if key is not None and item is not None:
            # Add the item to the cache
            self.cache_data[key] = item

            # Update the last added key
            if key != self.last_key:
                self.last_key = key

            # Check if we need to evict an item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Evict the last added item (LIFO)
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

                # Update last_key after deletion
                self.last_key = key

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        return self.cache_data.get(key, None)
