#!/usr/bin/python3
def uppercase(str):
    if 97 <= ord(str) <= 122:
        print("{}".format(str.upper()), end="")