#!/usr/bin/env python3


file = open("Army_PT_Test2file.txt", "r")
data = file.readlines()

for line in data:
    words = line.split()

print("age : {}\ngender : {}\nraw push up score : {}".format(words[1],words[4],words[6]))



file.close
