#!/usr/bin/python3
"""Contains the MyInt class. """


class MyInt(int):
    """ Inherits from int and has '==' and '!=' operators inverted. """
    def __eq__(self, other):
        """Compares with another value and if equal, returns false
        vice versa.
        """
        return True if self > other or self < other else False

    def __ne__(self, other):
        """Compares with another value and if equal, returns false
        vice versa.
        """
        return True if not (self > other) and not (self < other)  else False
