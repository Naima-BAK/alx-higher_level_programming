#!/usr/bin/python3
def print_last_digit(num):
    if num > 0:
        lastDigit = num % 10
    else:
        lastDigit = (num * -1) % 10
    print(lastDigit, end="")
    return lastDigit
