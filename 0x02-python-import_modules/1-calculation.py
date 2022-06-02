#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
a = 10
b = 5
c = str(a)
d = str(b)
u = str(add(a, b))
v = str(sub(a, b))
w = str(mul(a, b))
x = str(div(a, b))
print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}\
        ".format(c, d, u, c, d, v, c, d, w, c, d, x))
