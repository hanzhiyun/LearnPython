#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'

from functools import reduce


def prod(l):
    return reduce(lambda x, y: x * y, l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
