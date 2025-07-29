#!/usr/bin/env python3
'''sum mixed list'''


from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    '''sum of mixed list'''
    sum = 0
    for item in mxd_lst:
        sum = sum + item
    return sum
