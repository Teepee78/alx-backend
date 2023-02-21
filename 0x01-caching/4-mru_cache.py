#!/usr/bin/env python3
"""Defines MRUCache class"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
                discard = self.order[-1]
                print("DISCARD: {}".format(discard))
                self.cache_data.pop(discard)
                self.order.pop(-1)

            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """Gets a key from the cache

        Args:
            key: key

        Returns:
            None: If the key is not found else the cached value
        """

        if key is not None:
            item = self.cache_data.get(key)
            if item is not None:
                new = self.order.pop(self.order.index(key))
                self.order.append(new)

            return item
        return None
