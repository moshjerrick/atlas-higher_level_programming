#!/usr/bin/python3



def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not type(int, float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    result_matrix = []

    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(element / divisor)
        result_matrix.append(divided_row)
    return result_matrix