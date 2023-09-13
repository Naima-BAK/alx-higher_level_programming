#!/usr/bin/python3
"""
 the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r', encoding='utf-8') as f:
        listL = []
        while True:
            line = f.readline()
            if line == "":
                break
            listL.append(line)
            if search_string in line:
                listL.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(listL)
