#!/usr/bin/python3
"""
This module contains a class square
that inherits from (9-base_geometry.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Init a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        print str
        """
        return "[square] {}/{}".format(self.__width, self.__height)
