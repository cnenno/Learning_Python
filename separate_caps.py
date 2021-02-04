#!/usr/bin/env python3

s = "HbideVbxncC"

def accum(s):
#    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
    print('-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)))

accum(s)
