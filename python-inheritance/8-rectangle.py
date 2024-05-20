#!/usr/bin/python3
"""This module contains a class Rectangle
    that inherits from (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class"""
    def __init__(self, width, height):
        """ Init a Rectangle """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
