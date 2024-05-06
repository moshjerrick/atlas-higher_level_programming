#!/usr/bin/python3
def element_at(my_list, idx):
    for num in my_list:
        print("{:d}".format(num))
    if idx < 0:
        return None
    if idx > my_list:
        return None