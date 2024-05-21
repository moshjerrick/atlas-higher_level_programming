#!/usr/bin/python3
"""
Defining function to_json_string
"""


import json


def to_json_string(my_obj):
    """ Returning JSON representation of an object """
    return json.dumps(my_obj)
