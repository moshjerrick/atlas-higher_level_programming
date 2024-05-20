#!/usr/bin/python3
"""
Returning True if object is an instance of 
class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    checks to see if object is an instance
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
    