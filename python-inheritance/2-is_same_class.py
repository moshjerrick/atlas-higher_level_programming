#!/usr/bin/python3
"""
Defining a class-checking function
"""


def is_same_class(obj, a_class):
    """
     checking if obj is exact instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False