#!/usr/bin/python3
"""
1. FIFO caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class  inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Class properties Initialization
        """

        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value for the key.
        """

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.isFull():
                self.discardOutput()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """

        return self.cache_data.get(key, None)

    def isFull(self):
        """
        Checks if the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS.
        """

        return len(self.cache_data) >= self.MAX_ITEMS

    def discardOutput(self):
        """
        Print DISCARD: with the key discarded and following by a
        new line
        """

        poppedItem = self.queue.popleft()
        del self.cache_data[poppedItem]
        print("DISCARD: " + str(poppedItem))
