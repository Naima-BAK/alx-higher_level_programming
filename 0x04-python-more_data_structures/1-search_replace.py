#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for index in my_list:
        if index == search:
            list.append(replace)
        else:
            list.append(index)
    return list
