#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a // b
        print("{}".format(result))
    except ZeroDivisionError:
        print("{}".format("Divide by zero!!!!"))
    else: print("{}".format(result))
    finally:
        print({} {}.format("Inside result:", result))
