#!/usr/bin/python3
""" Contains the BaseGeometry class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that defines a rectangular shape. """
    def __init__(self, width, height):
        """ Initializes the rectangle object. """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ Calculates the are of the reactangle. """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
