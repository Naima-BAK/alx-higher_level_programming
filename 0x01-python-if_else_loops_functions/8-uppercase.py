#!/usr/bin/python3
def uppercase(str):
    upperCase = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            upperCase += chr(ord(character) - 32)
        else:
            upperCase += character
    print("{}".format(upperCase))
