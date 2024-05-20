#!/usr/bin/python3
"""
Creates class named BaseGeometry
"""


class BaseGeometry:
    """ Empty Class """
    def area(self):
        """ raises exceptions"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ Validates intergers"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
