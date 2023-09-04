#!/usr/bin/python3
"""
My Rectangle class
"""


class Rectangle:
    """Representation of Rectangle"""

    def __init__(self, width=0, height=0):
        """initializ a Rectangle class
        Args:
            width (int): The width.
            height (int): The height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
                 
        self.__height = value

    def area(self):
        """the area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """the printable representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for index in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if index != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
