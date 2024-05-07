#!/usr/bin/python3
def safe_print_integer(value):
    if value == 0
        return False
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
