#!/usr/bin/env python3

import re

strng = "This website is for losers LOL!"

def disemvowel(strng):
    return strng.translate(None, "aeiouAEIOU")

disemvowel(strng)
print(strng)

def disemvowel1(strng):
    return "".join(c for c in strng if c.lower() not in 'aeiou')

disemvowel1(strng)
print(strng) 


#import re
def disemvowel2(strng):
    return re.sub('[aeiou]', '', strng, flags = re.IGNORECASE)

disemvowel2(strng)
print(strng) 


def disemvowel3(strng):
    return strng.translate(None, 'aeiouAEIOU')


disemvowel3(strng)
print(strng) 


