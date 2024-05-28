#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
       super().__init__(size, size, x, y, id)