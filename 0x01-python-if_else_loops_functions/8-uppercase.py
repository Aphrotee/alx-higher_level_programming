#!/usr/bin/python3

def uppercase(sstr):
    c = len(sstr)
    if (c != 1) and (c != 0):
        for a in range(0, c):
            b = ord(sstr[a])
            if (b >= 97) and (b <= 122):
                b = b - 32
            print("{}".format(chr(b)), end="")
    print("")
