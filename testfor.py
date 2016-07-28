#!/usr/bin/env python2
# coding=utf-8
__author__ = 'Hanzhiyun'

a = range(6)
print a

a = range(1, 6)
print a

a = range(0, 8, 2)
print a

a = range(3, 31, 3)
print a


# for 循环
for i in range(5):
    print i

# 求和sum
n_sum = 0
for i in range(10):
    n_sum += i
    print n_sum

# while循环
# This while loop calculates the sum of 0 through 9 (including 9) and
# places it in the variable "n_sum"
n_sum = 0
i = 0
while i < 10:
    n_sum += i
    print n_sum
    i += 1


