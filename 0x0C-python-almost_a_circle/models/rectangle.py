#!/usr/bin/python3
"""Contains the rectangle class. """
from models.base import Base

class Rectangle(Base):
    """ A class that defines a rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises the rectangle object. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """Retrieves the width property. """
        return self.__width


    @width.setter
    def width(self, value):
        """Sets the width property. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """Retrieves the height property. """
        return self.__height


    @height.setter
    def height(self, value):
        """Sets the height property. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """Retrieves the x property. """
        return self.__x


    @x.setter
    def x(self, value):
        """Sets the x property. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """Retrieves the y property. """
        return self.__y


    @y.setter
    def y(self, value):
        """Sets the y property. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value



    def area(self):
        """ Calculates and returns the area of object. """
        return self.__width * self.__height


    def display(self):
        """Prints the rectangle to stdout. """
        i = 0
        while i < self.__y:
            print()
            i += 1
        for y in range(self.__height):
            j = 0
            while j < self.__x:
                print(" ", end="")
                j += 1
            for x in range(self.__width):
                print("#", end="")
            if y + 1 < self.__height:
                print()
        print()


    def __str__(self):
        """Returns information about the object. """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.__class__.__name__,
                                                            self.id, self.__x, self.__y,
                                                            self.__width, self.__height)


    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        l = len(args)
        if l > 0:
            if args[0] is None:
                self.id = Rectangle.increment_nb()
            else:
                self.id = args[0]
        if l > 1:
            self.width = args[1]
        if l > 2:
            self.height = args[2]
        if l > 3:
            self.x = args[3]
        if l > 4:
            self.y = args[4]
        if l == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of object."""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
