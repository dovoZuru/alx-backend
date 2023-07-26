#!/usr/bin/python3
"""
4. MRU Caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialization of class properties
        """

        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for
        the key
        """

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.isFull():
                self.printDiscardedOutput()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """

        return self.cache_data.get(key, None)

    def isFull(self):
        """
        Check if the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """

        return len(self.cache_data) >= self.MAX_ITEMS

    def printDiscardedOutput(self):
        """
        Print DISCARD: with the key discarded and following by a
        new line
        """

        poppedItem = self.queue.pop()
        del self.cache_data[poppedItem]
        print("DISCARD: " + str(poppedItem))
