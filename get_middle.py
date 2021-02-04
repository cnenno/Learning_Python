#!/usr/bin/env python3

s = "ABCDE"
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
    print(s[i:-i] or s)

get_middle(s)
