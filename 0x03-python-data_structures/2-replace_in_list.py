#!/usr/bin/python3
def replace_in_list(the_list, the_index, e):
    if the_index < 0 or the_index >= len(the_list):
        return the_list
    the_list[the_index] = e
    return the_list
