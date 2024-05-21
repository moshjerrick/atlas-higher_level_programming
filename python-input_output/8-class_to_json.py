#!/usr/bin/python3
"""
Defining clast_to_json function
"""


def class_to_json(obj):
    """ Converts objects attributes to dictionary v"""
    return obj.__dict__
