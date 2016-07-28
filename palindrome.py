#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'


def is_palindrome(n):
    return str(n)[::-1] == str(n)

output = filter(is_palindrome, range(1, 1000))
print(list(output))
