#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = my_list[:x]
    for item in result:
        try:
            print("{:d}".format(item))
        except IndexError:
            print()
    return result
