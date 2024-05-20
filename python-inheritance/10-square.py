#!/usr/bin/python3
"""
This module contains a class square
that inherits from (9-base_geometry.py).
"""

BaseGeometry = __import__('9-base_geometry').BaseGeometry

class Square(BaseGeometry):
    """ Square Class """
    def __init__(self, size):
        """ Init a Square """
        self.integer_validator("size". size)
        self.__size = size
        super().__init__(size, size)
