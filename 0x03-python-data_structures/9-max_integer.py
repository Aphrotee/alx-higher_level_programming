#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    d = 0
    for i in my_list:
        if (i > d):
            d = i
        else:
            continue
    return d
