#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for num in row:
            print("{:d}".format(num), end="")

        print()
