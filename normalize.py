#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'


def normalize(name):

    name = name[0].upper() + name[1:].lower()
    return name
    # return name.capitalize()  #Python 自带的函数使首字母大写，其余小写

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
