#!/usr/bin/python3
"""
This module provides a function to retrieve the list of attributes and methods
available for any given object.
"""

def lookup(obj):
    """
    Returns a list of attributes and methods available for the specified object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the names of available attributes
              and methods of the object.
    """
    return dir(obj)
