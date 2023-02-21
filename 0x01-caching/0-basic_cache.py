#!/usr/bin/env python3
"""Defines BasicCache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Caches a key/value pair

        Args:
            key: key
            item: item to cache
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

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
