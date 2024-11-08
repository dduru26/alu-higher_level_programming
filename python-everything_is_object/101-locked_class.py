#!/usr/bin/python3
"""This module defines a LockedClass that restricts dynamic attribute creation."""

class LockedClass:
    """
    A class that only allows the creation of a single dynamic attribute 'first_name'.

    The LockedClass restricts the user from creating any additional attributes
    dynamically, other than the specified 'first_name' attribute.
    """
    
    __slots__ = ['first_name']
