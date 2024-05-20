#!/usr/bin/python3
"""
Check for same class or if inherited from
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
