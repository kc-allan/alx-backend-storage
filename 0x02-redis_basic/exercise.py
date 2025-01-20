#!/usr/bin/env python3
"""
This is a simple exercise to test your understanding of Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    A simple cache class that stores data in Redis
    """

    def __init__(self):
        """
        Initialize the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the cache and return the ID
        :param data: The data to store
        :return: The ID of the stored data
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Get the data from the cache
        :param key: The key of the data to get
        :param fn: The function to apply to the data
        :return: The data from the cache
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Get the data from the cache as a string
        :param key: The key of the data to get
        :return: The data from the cache as a string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get the data from the cache as an integer
        :param key: The key of the data to get
        :return: The data from the cache as an integer
        """
        return self.get(key, int)
