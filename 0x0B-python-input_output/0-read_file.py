#!/usr/bin
"""
This module provides the function "read_file".
"""


def read_file(filename=""):
    """
    This function reads a file and prints it to the stdout.
    """

    if len(filename) == 0:
        return
    with open(filename, 'r', encoding="UTF-8") as fd:
        filee = fd.readlines()
        for a in range(len(filee)):
            print(filee[a], end='')
