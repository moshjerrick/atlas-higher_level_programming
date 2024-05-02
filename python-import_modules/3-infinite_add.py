#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = [int(arg) for arg in sys.argv[1:]]
    total = sum(args)
    print("{}".format(total))
