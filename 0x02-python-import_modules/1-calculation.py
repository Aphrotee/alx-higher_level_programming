#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
a = 10
b = 5
u = str(add(a, b))
v = str(sub(a, b))
w = str(mul(a, b))
x = str(div(a, b))
a = str(a)
b = str(b)
print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}\
        ".format(a, b, u, a, b, v, a, b, w, a, b, x))
