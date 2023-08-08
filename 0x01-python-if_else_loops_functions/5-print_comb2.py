#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        line = "\n"
    else:
        line = ", "
    print("{:02d}".format(num), end=line)
