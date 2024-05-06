#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if (set_1 or set_2):
        return list(set_1 or set_2)
    else:
        return []
