#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = [int(args) for arg in sys.argv[1:]]
    total = sum(arg)
    print("{}".format(total))