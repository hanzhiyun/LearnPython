#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'


def foo(s):
    n = int(s)
    # print('>>>n = %d' % n)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


main()
