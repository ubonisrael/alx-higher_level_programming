#!/usr/bin/python3
""" Contains the BaseGeometry class. """


class BaseGeometry:
    """ A class that defines a geometric shape. """

    def area(self):
        raise Exception('area() is not implemented')
