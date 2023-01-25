#!/usr/bin/python3
"""
MRU Cache Module

Contains MRU Cache class
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache system. """

    def __init__(self):
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """ Put function. """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                del self.cache_data[self.last]

            self.last = key

    def update(self, key):
        """ Updates cache history """
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)

    def get(self, key):
        """ Get function. """
        if key and key in self.cache_data:
            self.last = key
            return self.cache_data.get(key)
        return None
