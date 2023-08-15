#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        mul_ret = (0, None)
        return mul_ret
    else:
        result = (size, sentence[0:1])
        return result
