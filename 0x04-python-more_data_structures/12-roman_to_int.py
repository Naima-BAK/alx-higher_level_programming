#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    r = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and \
           values[roman_string[i]] < values[roman_string[i + 1]]:
            r -= values[roman_string[i]]
        else:
            r += values[roman_string[i]]
    return r
