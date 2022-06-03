#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    u = str(add(a, b))
    v = str(sub(a, b))
    w = str(mul(a, b))
    x = str(div(a, b))
    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}\
        ".format(a, b, u, a, b, v, a, b, w, a, b, x))
