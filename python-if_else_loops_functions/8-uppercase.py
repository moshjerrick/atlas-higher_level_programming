#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= chr(ord(char) -32):
            print("{}".format (str), end="")