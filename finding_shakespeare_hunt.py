#!/usr/bin/env python3

import urllib.request
import shutil
import re
from collections import Counter

with urllib.request.urlopen('http://www.gutenberg.org/files/100/100-0.txt') as response, open("file_name", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

def findgreat():
    with open("file_name", "r") as file:
        for x in file:
            if "some achieve greatness" in x.lower():
                print(x.split(".")[0].lstrip(" "))
def names():
    l = []
    with open("file_name", "r") as file:
        for x in file:
            for c in ('Bianca','Caesar','Cymbeline','Hamlet','Henry','Juliet','Macbeth','Ophelia','Othello','Romeo','Rosalind','Viola'):
                if c.lower() in x.lower():
                    l.append(c)
        print(Counter(l))

findgreat()

names()
