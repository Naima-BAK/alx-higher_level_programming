#!/usr/bin/python3
"""My Rectangle class."""


class Rectangle:
    """Representation of rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.
        Args:
            width (int): The width.
            height (int): The height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectangle1, rectangle2):
        """the greater area.
        Args:
            rectangle1 (Rectangle): The first Rectangle.
            rectangle2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If rectangle1 or rectangle2 is not a Rectangle.
        """
        if not isinstance(rectangle1, Rectangle):
            raise TypeError("rectangle1 must be an instance of Rectangle")
        if not isinstance(rectangle2, Rectangle):
            raise TypeError("rectangle2 must be an instance of Rectangle")
        if rectangle1.area() >= rectangle2.area():
            return (rectangle1)
        return (rectangle2)

    def __str__(self):
        """Return the printable representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """the string representation"""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """delete the Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
