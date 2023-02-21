#!/usr/bin/env python3
"""Defines FIFOCache class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Init method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Caches a key/value pair

        Args:
            key: key
            item: item to cache
        """

        if key is not None and item is not None:
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                # Discard
                discard = self.order[0]
                print("DISCARD: {}".format(discard))
                self.order.pop(0)
                self.cache_data.pop(discard)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Gets a key from the cache

        Args:
            key: key

        Returns:
            None: If the key is not found else the cached value
        """

        if key is not None:
            return self.cache_data.get(key)
        return None
