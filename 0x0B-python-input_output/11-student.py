#!/usr/bin/python3
"""Contains the student class. """


class Student:
    """Defines a student. """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a
        student instance.
        """
        if attrs is None:
            return self.__dict__
        obj = {}
        for v in self.__dict__:
            if v in attrs:
                obj[v] = self.__dict__[v]
        return obj

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance. """
        keys_list = list(self.__dict__.keys())
        for k in keys_list:
            self.__dict__.pop(k)
        for v in json:
            self.__dict__[v] = json[v]
