#!/usr/bin/python3
"""
Defining read_file function
"""


def read_file(filename=""):
    """
    Opening a text file and then printing it
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
