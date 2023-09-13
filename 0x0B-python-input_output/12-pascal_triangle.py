#!/usr/bin/python3
""" my mùodule """


def pascal_triangle(n):
    """ Pascal's triangle """
    if n <= 0:
        return []

    new_triangle = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = new_triangle[i-1][j-1] + new_triangle[i-1][j]
        new_triangle.append(row)

    return new_triangle
