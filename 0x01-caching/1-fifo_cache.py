#!/usr/bin/python3
"""
Fifo Cache Module

Contains Fifo Cache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Fifo Cache system. """

    def put(self, key, item):
        """ Put function. """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            delete = sorted(self.cache_data)[0]
            print("DISCARD: {}".format(delete))
            del self.cache_data[delete]

    def get(self, key):
        """ Get function. """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
