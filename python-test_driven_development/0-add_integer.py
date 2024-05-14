#!/usr/bin/python3
# Adding ints and floats after casing them to ints"""
def add_integer(a, b=98):
    #Add two numbers after converting them to integers.

    #Args:
        #a (int, float): The first number to be added.
        #b (int, float): The second number to be added. Default is 98.
    if type(a is not type(int, float)):
        raise TypeError("a must be an integer")
    if type(b is not type(int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
