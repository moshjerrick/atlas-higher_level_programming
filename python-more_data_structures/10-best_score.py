#!/usr/bin/python3
def best_score(a_dictionary):
    keymax = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
