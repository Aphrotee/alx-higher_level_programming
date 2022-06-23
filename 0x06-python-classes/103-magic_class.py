#!/usr/bin/python3

import dis
import math


class MagicClass:


     def __init__(self, radius=0):
        if type(radius) != float and type(radius) != int:
            raise TypeError("radius must  be a number")
        else:
            self.__radius = radius


    def area(self):
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        return (2 * math.pi * self.__radius)
