#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or if it is an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or an instance of a class
    that inherited from a_class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
              False otherwise.
    """
    return isinstance(obj, a_class)
