#!/usr/bin/python3
"""
Module Devide Matrix """


def matrix_divided(matrix, div):
    """
    Devides elements in a matrix

    Args:


    Raise:
        TypeError: div isnt in or float
        TypeError: matrix is not a list of list of numbers
        zerodivision error: div is 0

    Return: New matrix divided
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    result_matrix = []

    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(element / divisor)
        result_matrix.append(divided_row)
    return result_matrix
