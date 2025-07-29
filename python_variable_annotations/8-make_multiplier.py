#!/usr/bin/env python3
''' make_multiplier function '''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' make_multiplier '''
    def mul_function(val: float) -> float:
        return multiplier * val
    return mul_function
