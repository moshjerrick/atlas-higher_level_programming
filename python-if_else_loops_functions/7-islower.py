#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    is_lower = 97 <= ascii_value <= 122
    print("True" if is_lower else "False", end="")
