#!/usr/bin/python3
"""
LRU Cache Module

Contains LRU Cache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache system. """

    def __init__(self):
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ Put function. """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                delete = self.history[0]
                print("DISCARD: {}".format(delete))
                del self.cache_data[delete]
                self.history.pop(0)

            self.update(key)

    def update(self, key):
        """ Updates cache history """
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)

    def get(self, key):
        """ Get function. """
        if key and key in self.cache_data:
            self.update(key)
            return self.cache_data.get(key)
        return None
