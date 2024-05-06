#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.items())

    sorted_dict = {}
    for key, value in sorted_list:
        sorted_dict[key] = value

    print(sorted_dict)