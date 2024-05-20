#!/usr/bin/python3
"""
Returning True if object is an instance of 
class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    checks to see if object is an instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
    