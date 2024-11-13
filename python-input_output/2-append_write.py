#!/usr/bin/python3
"""
This module provides a function to append a string to a text file.
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file and returns
    the number of characters written.
    """

    with open(filename, "a", encoding="utf-8") as f:
        charnum = f.write(text)
        return charnum
