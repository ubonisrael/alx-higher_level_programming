#!/usr/bin/python3
"""Contains the student class. """


class Student:
    """Defines a student. """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a
        student instance.
        """
        return self.__dict__
