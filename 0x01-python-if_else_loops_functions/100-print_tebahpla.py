#!/usr/bin/python3
def uppercase(str):
    upperCase = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            upperCase += chr(ord(character) - 32)
        else:
            upperCase += character
    return upperCase


for i in range(122, 97 - 1, -1):
    if i % 2 == 1:
        i = ord(uppercase(chr(i)))
    print("{}".format(chr(i)), end='')
