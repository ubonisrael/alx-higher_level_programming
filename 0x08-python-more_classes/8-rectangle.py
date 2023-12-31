#!/usr/bin/python3
""" Contains a rectangle class. """


class Rectangle:
    """ Creates a rectangle object. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle object. """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Calculates and returns the area of the rectangle. """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle. """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for y in range(self.__height):
            for x in range(self.__width):
                shape += "{}".format(self.print_symbol)
            if y + 1 < self.__height:
                shape += "\n"

        return shape

    def __repr__(self):
        """ Return a string representation of the rectangle to be able to
        recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints a goodbye message then deletes an instance. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
