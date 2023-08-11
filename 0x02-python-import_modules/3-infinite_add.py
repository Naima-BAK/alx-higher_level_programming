#!/usr/bin/python3
from sys import argv
sum = 0
for count in argv[1:]:
    sum += int(count)
print("{:d}".format(sum))
