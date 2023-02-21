#!/usr/bin/env python3
"""Defines LFUCache class"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Init method"""
        super().__init__()
        self.order = []
        self.count = {}

    def discard(self):
        """Returns the key of the item to delete"""

        # Sort self.count
        count = sorted(self.count.items(), key=lambda x: x[1])
        # print("count: ", count)
        # Get the least frequently used items
        discards = []
        for i in range(len(count)):
            # the number of times the least recently used
            # item was used
            if count[i][1] == count[0][1]:
                discards.append(count[i][0])
        if len(discards) == 1:
            # print("discards: ", discards)
            return discards[0]
        else:
            for key in self.order:
                if key in discards:
                    # print(f"Order: {self.order}, key: {key}")
                    return key

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
                discard = self.discard()
                print("DISCARD: {}".format(discard))
                self.cache_data.pop(discard)
                self.order.pop(self.order.index(discard))
                self.count.pop(discard)

            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            if key not in self.count:
                self.count[key] = 0
            else:
                self.count[key] += 1

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
                self.count[key] += 1

            return item
        return None


my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()
