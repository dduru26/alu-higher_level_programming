#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):  # Loop from the last index to the first
        print("{:d}".format(my_list[i]))  # Print each integer using str.format()
