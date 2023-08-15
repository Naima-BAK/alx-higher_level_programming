#!/usr/bin/python3
def new_in_list(my_list, index, e):
    if index < 0 or index >= len(my_list):
        return my_list.copy()
    new = my_list.copy()
    new[index] = e
    return new
