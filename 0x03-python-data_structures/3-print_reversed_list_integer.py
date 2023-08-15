#!/usr/bin/python3
def print_reversed_list_integer(the_list=[]):
    if the_list is not None:
        for count in range(len(the_list) - 1, - 1, - 1):
            print("{:d}".format(the_list[count]))
