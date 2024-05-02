#!/usr/bin/python3
from calculator_1 import calculator

def add(a, b):
    result = calculator(a, b)
    print("{} + {} = {}".format(a, b, result))

def subtract(a, b):
    result = calculator(a, b, '-')
    print("{} - {} = {}".format(a, b, result))

def multiply(a, b):
    result = calculator(a, b, '*')
    print("{} * {} = {}".format(a, b, result))

def divide(a, b):
    result = calculator(a, b, '/')
    print("{} / {} = {}".format(a, b, result))

if __name__ == "__main__":
    a = 10
    b = 5

    add(a,b)
    subtract(a,b)
    multiply(a, b)
    divide(a, b)