#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer in a list."""
    if not my_list:
        return None
    
    biggest = my_list[0]  # Start with the first element as the biggest
    for num in my_list:
        if num > biggest:
            biggest = num  # Update biggest if a larger number is found
    return biggest
