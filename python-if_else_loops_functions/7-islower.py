#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    c = 97 <= ascii_value <= 122
    print("True" if (c) else "False", end="")
