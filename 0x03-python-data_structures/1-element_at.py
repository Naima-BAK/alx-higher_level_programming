#!/usr/bin/python3
def element_at(the_list, the_index):
    if the_index < 0 or the_index >= len(the_list):
        return None
    return the_list[the_index]
