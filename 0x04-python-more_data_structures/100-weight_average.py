#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    s = 0
    w = 0

    for s2, w2 in my_list:
        s += s2 * w2
        w += w2
    return s / w
