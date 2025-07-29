#!/usr/bin/env python3
'''sum of a list'''


from typing import List

def sum_list(input_lists: list[float]) -> float:
    '''sum of a list'''
    sum = 0
    for item in input_lists:
        sum = sum + item
    return sum(input_lists)
