#!/usr/bin/python3

"""
This module supplies the function "text_indentation"
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        return
    for char in text:
        print("{}".format(char), end="")
        if char == "." or char == "?" or char == ":":
            print("\n")
    print("")
