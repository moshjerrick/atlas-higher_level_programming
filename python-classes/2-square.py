#!/usr/bin/python3
"""Defining a class square with size."""


class Square:
    """This be Square"""

    def __init__(self, size=0):
        """Initialize the Square with size"""

        if type(size) != int:
            raise TypeError
        """size must be an int"""
        if size < 0:
            raise ValueError
        """size must be above 0"""
        self.__size = size
