#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'


def triangles():
    tri = [1]
    while True:
        yield tri
        tri = [sum(i) for i in zip([0] + tri, tri + [0])]
    return

n = 0
for t in triangles():
    print(t)
    n += 1
    if 10 == n:
        break
