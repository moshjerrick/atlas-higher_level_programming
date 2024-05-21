#!/usr/bin/python3
""" Defining the function load_from_json_file """


import json


def load_from_json_file(filename):
    """ Creates an onject from a json file"""
    with open(filename, 'r') as f:
        json_str = f.read()
        return json.loads(json_str)
