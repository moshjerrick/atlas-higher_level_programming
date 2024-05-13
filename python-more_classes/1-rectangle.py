#!/usr/bin/python3
"""Defining a class rectangle."""


class Rectangle:
    """This be Rectangle"""
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = height

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("height must be an integer")

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("width must be an integer")


