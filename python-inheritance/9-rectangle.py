#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It validates width and height as positive integers, implements area(),
and defines the __str__ and __repr__ methods for printing.
"""


class BaseGeometry:
    """
    A base class for geometric shapes. Contains methods to validate integers
    and raise an exception for the area method.
    """

    def area(self):
        """
        Raises an exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

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


class Rectangle(BaseGeometry):
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
