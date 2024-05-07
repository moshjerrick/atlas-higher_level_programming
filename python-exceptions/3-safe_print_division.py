#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except:
        x = None
    finally:
        print({}+{}.format("Inside result:", x))
        return x