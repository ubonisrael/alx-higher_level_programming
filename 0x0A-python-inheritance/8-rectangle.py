#!/usr/bin/python3
""" Contains the BaseGeometry class. """


class BaseGeometry:
    """ A class that defines a geometric shape. """

    def area(self):
        """ Raises an exception. """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates value of name attribute. """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ A class that defines a rectangular shape. """
    def __init__(self, width, height):
        """ Initializes the rectangle object. """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
