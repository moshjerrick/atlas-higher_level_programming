#!/usr/bin/python3
from calculator_1 import calculator
a = 10
b = 5
def add(a, b):
    print("{} + {} = {}".format(a, b, add(a, b)))

def subtract(a, b):
    print("{} - {} = {}".format(a, b, subtract(a, b)))

def multiply(a, b):
    print("{} * {} = {}".format(a, b, multiply(a,b)))

def divide(a, b):
    print("{} / {} = {}".format(a, b, divide(a, b)))

if __name__ == "__main__":