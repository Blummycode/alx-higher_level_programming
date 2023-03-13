#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > big:
            big = my_list[j]

    return (big)
