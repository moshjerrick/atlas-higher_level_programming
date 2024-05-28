#!/usr/bin/python3
"""
Getting that Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json str representing dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

