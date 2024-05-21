#!/usr/bin/python3
"""
Defining function from_json_string
"""


import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON str """
    return json.loads(my_str)
