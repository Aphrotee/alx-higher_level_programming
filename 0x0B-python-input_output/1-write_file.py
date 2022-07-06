#!/usr/bin/python3
"""
This module supplies the function "write_file".
"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="UTF-8") as fd:
        a = fd.write(text)
    return a
