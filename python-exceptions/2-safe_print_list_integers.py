#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = my_list[:x]
    for item in result:
        try:
            print("{:d}".format(item), end="")
        except ValueError:
            print()
    return result
