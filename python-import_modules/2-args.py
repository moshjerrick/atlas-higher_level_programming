#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_number = len(sys.argv) - 1
    print("{} {}".format(arg_number, "argument:" if arg_number == 1 else "arguments:"))
    for i, arg in enumerate(sys.argv[1:], start = 1):
        print("{}: {}".format(i, arg))