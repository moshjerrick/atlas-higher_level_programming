#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    print("{:d}{:d}".format(idx, element_at(list, idx))
