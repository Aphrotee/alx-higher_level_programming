#!/usr/bin/python3

def uppercase(sstr):
    c = len(sstr)
    if c == 0:
        return
    if c != 1:
        for a in range(0, c-1):
            b = ord(sstr[a])
            if (b >= 97) and (b <= 122):
                b = b - 32
            print("{}".format(chr(b)), end="")
    b = ord(sstr[c-1])
    if (b >= 97) and (b <= 122):
        b -= 32
    print("{}".format(chr(b)))
