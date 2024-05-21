#!/usr/bin/python3
"""
init class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            if hasattr(self, i):
                dictionary[i] = getattr(self, i)
        return dictionary

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
