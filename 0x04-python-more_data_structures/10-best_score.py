#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        bestScore = list(my_dict.keys())[0]
        for index in my_dict:
            if my_dict[index] > my_dict[bestScore]:
                bestScore = index
        return bestScore
    return None
