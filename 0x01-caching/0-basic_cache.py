#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class with unlimited caching """

    def put(self, key, item):
        """ Adds an item to the cache if key and item are not None """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        return self.cache_data.get(key, None)
