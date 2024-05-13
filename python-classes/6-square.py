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

    def my_print(self):
        # method to print a # according to the size value
        if not self.__size:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
    @property
    def position(self):
        #get position
        return self.__position

    @position.setter
    def position(self, value):

        if len(value) != 2 or type(value) != tuple:
            raise ValueError
        if type(value[0]) != int or value[0] < 0 or type(value[1]) != int or value[1 <0]:
            raise ValueError
        self.__position = value


