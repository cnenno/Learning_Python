#!/usr/bin/env python3

import re
names={
'Bianca':0,
'Caesar':0,
'Cymbeline':0,
'Hamlet':0,
'Henry':0,
'Juliet':0,
'Macbeth':0,
'Ophelia':0,
'Othello':0,
'Romeo':0,
'Rosalind':0,
'Viola':0,
}
with open ("file_name", "r") as searchfile:
        for line in searchfile:
                for k in names:
                        if k.lower() in line.lower():
                                names[k]+=1
        s = [(k, names[k]) for k in sorted(names, key=names.get, reverse=True)]
        for k,v in s:
                        print (k,v)
