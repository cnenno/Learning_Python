#!/usr/bin/env python3

def fake_bin(x):
    mystr = ""
    for a in x:
        if int(a) < 5:
            a = 0
            mystr = mystr + str(a)
        elif int(a) >= 5:
            a = 1
            mystr = mystr + str(a)
    return mystr
