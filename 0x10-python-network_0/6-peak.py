#!/usr/bin/python3
"""
This module provides a function that
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Returns the peak value in the list"""
    if type(list_of_integers).__name__ != 'list':
        return
    if len(list_of_integers) == 0:
        return
    pk = list_of_integers[0]
    i = 0
    j = -1
    while i < len(list_of_integers) / 2:
        if list_of_integers[i] >= list_of_integers[j]:
            temp = list_of_integers[i]
        else:
            temp = list_of_integers[j]
        if temp >= pk:
            pk = temp
        i += 1
        j -= 1
    return pk
