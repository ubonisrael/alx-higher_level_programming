#!/usr/bin/python3
""" Contains a rectangle class. """


class Rectangle:
    """ Creates a rectangle object. """
    def __init__(self, width=0, height=0):
        """ Initializes the rectangle object. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the rectangle's width. """
        return self.__width

    @property
    def height(self):
        """ Retrieves the rectangle's height. """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the rectangle's width. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the rectangle's height. """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
