#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Hanzhiyun'


def fact(n):
    """
    Simple fact only support number
    >>> fact(5)
    120
    >>> fact(2)
    2
    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError
    """
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()