#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'
from functools import reduce


def str2float(s):
    int_l = s.split('.')
    integer = str2int(int_l[0])
    if len(s) - len(int_l[0]) > 0:
        decimal = str2int(int_l[1]) / (10 ** len(int_l[1]))
        return integer + decimal
    else:
        return integer + 0.0


def char2num(ch):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print('str2float(\'123.456\') =', str2float('123.456'))
print('str2float(\'123456\') =', str2float('123456'))
