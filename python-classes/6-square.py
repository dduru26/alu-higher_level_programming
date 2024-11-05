#!/usr/bin/python3
"""This module defines a Square class with size and position attributes."""


class Square:
    """A class that defines a square with a size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with the given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): A tuple of two positive integers for
                              the position.

        Raises:
            TypeError: If size is not an integer or if position is not
                       a tuple of two positive integers.
            ValueError: If size is less than 0 or if position values
                        are not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square.

        Returns:
            tuple: The position of the square as a tuple of two integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, print an empty line.
        The position is used to determine the starting point of the square.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
