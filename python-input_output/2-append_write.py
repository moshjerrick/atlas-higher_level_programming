#!/usr/bin/python3
"""
Defining the append_write
"""


def append_write(filename="", text=""):
    """ Appending text to end of file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
    