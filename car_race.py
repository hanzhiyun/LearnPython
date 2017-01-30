#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Hanzhiyun'

from random import random
from functools import reduce


# time = 5
# car_positions = [1, 1, 1]
# while time:
#     # decrease time
#     time -= 1
#     print('')
#     for i in range(len(car_positions)):
#         # move car
#         if random() > 0.3:
#             car_positions[i] += 1
#         # draw car
#         print('-' * car_positions[i])


L = [0]*3
result = reduce(lambda ll, _: list(map(lambda x: (x+1) if random() > 0.3 else x, ll)), range(5), L)
print(list(result))


# def my_reduce(numbers, function, initial):
#     total = initial
#     for x in numbers:
#         total = function(total, x)
#     return total
#
#
# a = my_reduce(range(1, 10), lambda t, x: t + x, 0)
# b = my_reduce(range(1, 10), lambda t, x: t * x, 1)
# print(a,b)