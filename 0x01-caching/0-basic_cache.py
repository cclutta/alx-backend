#!/usr/bin/python3
"""
Base Cache Module

Contains Base Cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching sytem
    """
    def put(self, key, item):
        """ Put function. """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get function. """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
