#!/usr/bin/python3
from calculator_1 import calculator
a = 10
b = 5
def add(a, b):
    return calculator(a, b, '+')
def subtract(a, b):
    return calculator(a, b, '-')
def multiply(a, b):
    return calculator(a, b, '*')
def divide(a, b):
    return calculator(a, b, '/')
if __name__ == "__main__":