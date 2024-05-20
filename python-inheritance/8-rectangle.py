#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.interger_validator("width", width)
        self.interger_validator("height", height)
