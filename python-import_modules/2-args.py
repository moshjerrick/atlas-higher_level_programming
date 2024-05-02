#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print("{}".format("0 arguments."))
    elif arg_number == 1:
        print("{} {}".format(arg_number, "argument:"))
    else:
        print("{} {}".format(arg_number, "arguments:"))

    for i, arg in enumerate(sys.argv[1:], start = 1):
        print("{}: {}".format(i, arg))
