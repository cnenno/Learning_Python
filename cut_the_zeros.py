#!/usr/bin/env python3

def foo(n):
    if n == 0:
        return n
    result = str(n)
    s = str(n)
    for i in range(len(s)-1,0,-1):
        if s[i] == '0':
            result = s[0:i]
        else:
            return int(result)
    else:
        return n

print(foo(1450))
print(foo(960000))
print(foo(1050))
print(foo(-1050))
print(foo(100))
print(foo(999))
