#!/usr/bin/env python3

def main():

    x = input("Enter Age: ")
    y = input("Enter Gender (M or F): ")
    z = input("Enter raw pushup score: ")

    if (y == "M") or (y == "m"):
        y = "Male"
    elif (y == "F") or (y == "f"):
        y = "Female"
    else:
        y = "of unknown gender"

    print("The user entered the following:\n A {} year old {} performed {} pushups on the APFT.".format(x,y,z))

main()

