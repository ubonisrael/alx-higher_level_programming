#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    if a_dictionary is not None and len(a_dictionary) > 0:
        for k, v in a_dictionary.items():
            if v > (a_dictionary[max_score] if max_score is not None else 0):
                print(k)
                max_score = k
    return max_score
