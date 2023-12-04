#!/usr/bin/python3
""" Contains the BaseGeometry class. """


class BaseGeometry:
    """ A class that defines a geometric shape. """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} mus be greater than 0'.format(name))
