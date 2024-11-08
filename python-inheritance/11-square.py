#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It validates the size as a positive integer, implements the area() method,
and defines the string representation of the square for printing.
"""

class Rectangle:
    """
    A class representing a rectangle. Inherits from BaseGeometry.
    Validates and sets the width and height as private attributes.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height. Both are
        validated as positive integers using the integer_validator method.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        [Rectangle] <width>/<height>

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate the rectangle
        object with the same attributes.

        Returns:
            str: The string representation for recreating the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(Rectangle):
    """
    A class representing a square, inherited from Rectangle. 
    The square is validated and initialized with a single size attribute.
    """

    def __init__(self, size):
        """
        Initializes the Square instance with size. Size is validated as a 
        positive integer using the integer_validator method from Rectangle.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

        # Initialize the Square as a Rectangle with both width and height equal to size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square. Since it's a square, area = size * size.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square in the format:
        [Square] <width>/<height>

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
