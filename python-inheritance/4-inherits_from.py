#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited (directly or
    indirectly) from a_class, but not an instance of a_class itself.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False if obj
              is an instance of a_class or if it does not inherit from a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
