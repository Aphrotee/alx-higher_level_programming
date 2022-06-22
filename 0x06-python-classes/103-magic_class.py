#!/usr/bin/python3

from math import pi
"""
This is a module that provides a MagicClass Object for a
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

    def __init__(self, radius):
        if type(radius) != float or type(radius) != int:
            raise("radius must  be a number")
        else:
            self.__radius = radius

    def area(self):
        return (pi * (self.__radius ** 2))

    def circumference(self):
        return (2 * pi * self.__radius)
