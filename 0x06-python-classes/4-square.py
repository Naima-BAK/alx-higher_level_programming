#!/usr/bin/python3
"""
The Square class
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a square instance
        Args:
            size (int): The size of square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size.
        Returns:
            int: The size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size.
        Args:
            value (int): The size of square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area.
        Returns:
            int: The area of square.
        """
        return self.__size ** 2
