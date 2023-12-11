#!/usr/bin/python3
"""Contains the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an informal representation of the object."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                       self.id,
                                                       self._Rectangle__x,
                                                       self._Rectangle__y,
                                                       self._Rectangle__width)

    @property
    def size(self):
        """Retrieves the size property."""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Sets the size property."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the object."""
        length = len(args)
        if length > 0:
            self.id = args[0]
        if length > 1:
            self.size = args[1]
        if length > 2:
            self.x = args[2]
        if length > 3:
            self.y = args[3]
        if length == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of object."""
        return {'x': self._Rectangle__x, 'y': self._Rectangle__y,
                'id': self.id, 'size': self._Rectangle__width}
