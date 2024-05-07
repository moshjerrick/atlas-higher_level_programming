#!/usr/bin/python3
def safe_print_integer(value):
    if value == 0:
        return True
    try:
        value_str = str(value)
        if value_str.startswith('{') and value_str.endswith('}'):
            value_str = value_str[1:-1]
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
