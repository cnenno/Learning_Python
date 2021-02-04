#!/usr/bin/env python3

def main2():
    x = input("Enter Age: ")
    y = input("Enter Gender (M or F): ")
    z = input("Enter raw pushup score: ")

    if (y == "M") or (y == "m"):
        y = "Male"
    elif (y == "F") or (y == "f"):
        y = "Female"
    else:
        y = "of unknown gender"

    file = open("act42.txt","w")
    file.write("A {} year old {} performed {} pushups on the APFT.\n".format(x,y,z))
    file = open("act42.txt", "r")
    print(file.read())
    file.close

main2()
