#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    new_node = []
    for index in my_list:
        if index % 2 == 0:
            new_node.append(True)
        else:
            new_node.append(False)
    return new_node
