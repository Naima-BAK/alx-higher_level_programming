#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupA = tuple_a[:2]
    tupB = tuple_b[:2]
    tupA += (0,) * (2 - len(tupA))
    tupB += (0,) * (2 - len(tupB))
    sum = (tupA[0] + tupB[0], tupA[1] + tupB[1])
    return sum
