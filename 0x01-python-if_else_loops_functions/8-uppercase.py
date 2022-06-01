#!/usr/bin/python3

def uppercase(sstr):
    for a in range(0, len(sstr)-1):
        b = ord(sstr[a])
        if (b >= 97) and (b <= 122):
            b = b - 32
        print("{}".format(chr(b)), end="")
    b = ord(sstr[a+1])
    if (b >= 97) and (b <= 122):
        b -= 32
    print("{}".format(chr(b)))
