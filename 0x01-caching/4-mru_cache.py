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
        if key is not None and item is not None:
            """ If the key already exists,
            remove it from usage_order to update its position """
            if key in self.cache_data:
                self.usage_order.remove(key)

            # Add the item to the cache and mark it as most recently used
            self.cache_data[key] = item
            self.usage_order.append(key)

            """ If the cache exceeds the max size,
            discard the most recently used item """
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # The most recently used item is the last item in usage_order
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        if key is not None and key in self.cache_data:
            # Update usage order as this key is now the most recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
