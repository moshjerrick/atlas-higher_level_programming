#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_number = len(sys.argv) - 1
    print("{} {}".format(arg_number, "argument: "))
    for arg in sys.argv[1:]:
        print("{}".format(arg))