#!/usr/bin/python3
"""Module to perform addition of integers and floats."""

def add_integer(a, b=98):
    """Add two numbers after converting them to integers.

    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added. Default is 98.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Returns:
        int: The sum of the two numbers as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
