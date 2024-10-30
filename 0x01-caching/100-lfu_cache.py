#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class with LFU + LRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_freq = {}  # Track the frequency of access for each key
        self.access_order = []  # Track the order of access for LRU fallback

    def put(self, key, item):
        """ Adds an item to the cache with LFU + LRU eviction policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key's frequency and order
            self.usage_freq[key] += 1
            self.access_order.remove(key)
        else:
            # Add new item to cache, reset frequency, add to access order
            self.cache_data[key] = item
            self.usage_freq[key] = 1

        self.access_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find LFU item(s) - minimum frequency in usage_freq
            min_freq = min(self.usage_freq.values())
            lfu_keys = [k for k, v in self.usage_freq.items() if v == min_freq]

            # Use LRU if multiple LFU candidates
            if len(lfu_keys) > 1:
                # Choose LFU + LRU by access order
                lfu_key = next(k for k in self.access_order if k in lfu_keys)
            else:
                lfu_key = lfu_keys[0]

            # Discard LFU item and print
            del self.cache_data[lfu_key]
            del self.usage_freq[lfu_key]
            self.access_order.remove(lfu_key)
            print(f"DISCARD: {lfu_key}")

        # Add or update item after checking size
        self.cache_data[key] = item

    def get(self, key):
        """ Gets the value associated with a key in the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and order
        self.usage_freq[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
