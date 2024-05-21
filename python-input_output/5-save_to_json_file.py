#!/usr/bin/python3
"""
Defining function save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """ Writing an object to a text file using JSON """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
