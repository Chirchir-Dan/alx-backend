#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class with LFU + LRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        # Frequency of each key
        self.usage_freq = defaultdict(int)

        # Keeps track of access order by key
        self.access_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache with LFU + LRU eviction policy """
        if key is None or item is None:
            return

        # Update existing item
        if key in self.cache_data:
            self.cache_data[key] = item
            self._increment_frequency(key)
        else:
            # Add new item if cache is full, evict one if necessary
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_lfu_item()

            # Add item to cache, initialize frequency and order
            self.cache_data[key] = item
            self.usage_freq[key] = 1
            self.access_order[key] = None

    def get(self, key):
        """ Retrieve an item from the cache and update its frequency """
        if key is None or key not in self.cache_data:
            return None
        self._increment_frequency(key)
        return self.cache_data[key]

    def _increment_frequency(self, key):
        """
        Increment the frequency and update access order for LRU fallback
        """
        self.usage_freq[key] += 1
        self.access_order.move_to_end(key)  # Update order for LRU

    def _evict_lfu_item(self):
        """ Evict the least frequently used item, with LRU fallback """
        # Find the minimum frequency
        min_freq = min(self.usage_freq.values())
        # Collect all keys with that minimum frequency
        lfu_candidates = [
                k for k, freq in self.usage_freq.items() if freq == min_freq
                ]

        # Apply LRU by using the access order of keys with minimum frequency
        lfu_key = next(k for k in self.access_order if k in lfu_candidates)

        # Remove LFU item from all tracking structures
        del self.cache_data[lfu_key]
        del self.usage_freq[lfu_key]
        self.access_order.pop(lfu_key)

        # Print the key that was discarded
        print(f"DISCARD: {lfu_key}")
