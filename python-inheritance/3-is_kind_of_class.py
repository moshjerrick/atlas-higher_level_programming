#!/usr/bin/python3
"""
Check for same class or if inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Checks to see if its a object or instance of another class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
