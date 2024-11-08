#!/usr/bin/python3
"""
This module defines a class called BaseGeometry
with an area method that raises an exception.
"""


class BaseGeometry:
    """
    A base class for geometric shapes. Contains a method `area` 
    that raises an exception, meant to be implemented in subclasses.
    """

    def area(self):
        """
        Raises an exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
