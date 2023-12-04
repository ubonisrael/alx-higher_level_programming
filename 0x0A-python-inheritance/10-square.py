#!/usr/bin/python3
""" Contains the Square class. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that defines a square shape. """
    def __init__(self, size):
        """ Initializes the square object. """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ Calculates the area of the square. """
        return self.__size ** 2

    def __str__(self):
        """ Returns an informal string representation of the object. """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
