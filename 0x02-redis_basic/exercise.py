#!/usr/bin/env python3
"""
This is a simple exercise to test your understanding of Redis
"""
import redis
import uuid


class Cache:
    """
    A simple cache class that stores data in Redis
    """
    _redis = redis.Redis()

    def __init__(self):
        """
        Initialize the cache
        """
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        Store the data in the cache and return the ID
        :param data: The data to store
        :return: The ID of the stored data
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
