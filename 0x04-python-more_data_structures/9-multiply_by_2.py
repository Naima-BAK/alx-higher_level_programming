#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicti = {}
    for key, value in a_dictionary.items():
        dicti[key] = value * 2
    return dicti
