#!/usr/bin/python3
"""
Getting that Base
"""
import json
from os import path
import csv


class Base:
    """
    Base class attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init id attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
            temp_json = json.dumps(list_dictionaries)
            rturn temp_json


