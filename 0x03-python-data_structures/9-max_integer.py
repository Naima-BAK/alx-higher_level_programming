#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    max = my_list[0]
    for index in range(1, len(my_list)):
        if max < my_list[index]:
            max = my_list[index]
        else:
            continue
    return max
