#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class with an MRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Adds an item to the cache using MRU policy """
        if key is None or item is None:
            return

        # Update existing key to the most recent position
        if key in self.cache_data:
            self.usage_order.remove(key)
        # Add new item to cache
        self.cache_data[key] = item
        self.usage_order.append(key)

        # Check if cache size exceeds max limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used (last in `usage_order`)
            "Second-last as new item is last"
            mru_key = self.usage_order.pop(-2)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order: remove the key and add it to the end
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
