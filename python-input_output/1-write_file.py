#!/usr/bin/python3
"""
Defining the write_file function
"""


def write_file(filename="", text=""):
    """ Writing a string of text to a text file """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
