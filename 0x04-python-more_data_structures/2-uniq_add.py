#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniique = list(set(my_list))
    add = 0
    for index in uniique:
        add += index
    return add
