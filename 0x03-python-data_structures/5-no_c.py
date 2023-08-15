#!/usr/bin/python3
def no_c(string):
    string2 = ''
    for index in string:
        if index != 'c' and index != 'C':
            string2 += index
    return string2
