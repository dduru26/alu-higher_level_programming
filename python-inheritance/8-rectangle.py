#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes the Rectangle with width and
                                        height.
        __str__(self): Returns a string representation of the Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with the specified width and height after
        validation.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
