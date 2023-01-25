#!/usr/bin/python3
"""
Lifo Cache Module

Contains Lifo Cache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Lifo Cache system. """

    def __init__(self):
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """ Put function. """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(delete))
            del self.cache_data[self.last]

        self.last = key

    def get(self, key):
        """ Get function. """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
