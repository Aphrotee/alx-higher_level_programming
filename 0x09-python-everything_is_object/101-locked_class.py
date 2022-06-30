#!/usr/bin/python3
"""
This is the module that supplies the class LockedClass
"""


class LockedClass:
    """
    Class for initializing LockedClass object
    """

    def __init__(self):
        self.first_name = ""

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            raise AttributeError("'LockedClass' \
object has no attribute 'last_name'")
        else:
            self.__first_name = value
        object.__setattr__(self, key, value)
