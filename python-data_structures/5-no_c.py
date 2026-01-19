#!/usr/bin/python3
def no_c(str):
    newstr = ""
    for char in str:
        if char != 'c' and char != 'C':
            newstr += char
    return newstr
