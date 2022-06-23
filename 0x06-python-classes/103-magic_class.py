#!/usr/bin/python3

import dis
import math

"""
103-magic_class is a module that provides a MagicClass Object for a
Circle which has a private instance attribute "radius"
which must either be float or integer.
This class has a method to calculate the area of the circle
and a method to calculate the circumference of the circle
"""


class MagicClass:

    """
    This is a class Object for a
    Circle which has a private instance attribute "radius"
    which must either be float or integer.
    This class has a method to calculate the area of the circle
    and a method to calculate the circumference of the circle
    """


    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
