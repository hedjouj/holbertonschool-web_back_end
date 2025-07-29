#!/usr/bin/env python3
'''Complex types'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''complex types'''
    return (k, float(v ** 2))
