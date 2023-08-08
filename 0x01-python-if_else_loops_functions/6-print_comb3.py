#!/usr/bin/python3
for number1 in range(0, 9):
    for number2 in range(number1 + 1, 10):
        if number1 == 8:
            line = "\n"
        else:
            line = ", "
        print("{:d}{:d}".format(number1, number2), end=line)
