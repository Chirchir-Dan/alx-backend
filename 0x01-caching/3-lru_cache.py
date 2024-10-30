#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class with an LRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Adds an item to the cache using LRU policy """
        if key is not None and item is not None:
            # If the key is already in cache, remove it from usage_order to update its position
            if key in self.cache_data:
                self.usage_order.remove(key)

            # Add the item to the cache and update usage order
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If cache exceeds the maximum size, remove the least recently used item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # The least recently used item is the first item in usage_order
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        if key is not None and key in self.cache_data:
            # Update usage order because this key was recently accessed
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
