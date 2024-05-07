#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = my_list[:x]
    for i in result:
        try:
            print("{}".format(i))
        except IndexError:
            print()
    return result
