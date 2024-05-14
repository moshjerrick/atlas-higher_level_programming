#!/usr/bin/python3
"""Adding ints and floats after casing them to ints"""
def add_integer(a, b=98):
    if type(a is not type(int, float)):
        raise TypeError("a must be an integer")
    if type(b is not type(int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
