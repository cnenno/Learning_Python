#!/usr/bin/env python3

def binary_array_to_number(arr):
#    s = "".join(map(str, arr))
#    s = int.from_bytes(int(s), byteorder='big')

#   return int("".join(map(str, arr)), 2)
#   return int(''.join(str(a) for a in arr), 2)

    print(int("".join(map(str, arr)), 2))

binary_array_to_number([0,0,0,1])
