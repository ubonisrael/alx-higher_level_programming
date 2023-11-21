#!/usr/bin/python3
"""Corresponding code for MagicClass Bytecode. """
import dis

class MagicClass:
    """ Initiates a class for a circle. """
    def __init__(self, radius):
        """Initializes the circles attributes. """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ Calculates the area of the circle. """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Calculates the circumference of the circle. """
        return 2 * math.pi * self.__radius

dis.dis(MagicClass)
