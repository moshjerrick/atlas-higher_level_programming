#!/usr/bin/python3
"""Defining a class square with size."""


class Square:
    """This be Square"""

    def __init__(self, size=0):
        """Initialize the Square with size"""

        self.size = size

    @property
    def size(self):
        # getter setter return current size of square
        return (self.__size)
    
    @size.setter
    def size(self, value):
        # method to set size value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        # size must be an integer
        elif value < 0:
            raise ValueError("size must be >= 0")
        # size must be above 0
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
    

