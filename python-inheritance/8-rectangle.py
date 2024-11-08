#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry. It
validates the width and height as positive integers.
"""

from 7-base_geometry import BaseGeometry


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
