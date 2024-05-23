#!/usr/bin/python3
"""
Getting that Base
"""


class Base:
    """
    Base class attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init id attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
