#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = my_list[:x]
    for i in range(x):
        try:
            print("{}".format(result))
        except IndexError:
            print()
    return result
