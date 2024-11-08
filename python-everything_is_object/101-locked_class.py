#!/usr/bin/python3
"""This module defines a LockedClass that only allows a single attribute 'first_name'."""

class LockedClass:
    __slots__ = ['first_name']
