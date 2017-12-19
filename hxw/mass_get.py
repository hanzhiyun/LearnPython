#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-29 20:07:15
# @Author  : Han Zhiyun (hanzhiyun1995@foxmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os

filename = 'PMDA-40ODA-PLASMA.rxmolfra'
source = open(filename, 'r')
out = open('output.txt', 'w')
lines = source.readlines()
mass_sum = 0
mass = []

for line in lines:
    line = line.rstrip('\n')
    line_s = line.split()
    # print(line)

    if str.isdigit(line_s[0]):
        ite = int(line_s[0]) / 500
        # print(ite)
        if float(line_s[4]) > 100:
            # print(line_s[4])
            mass_sum += int(line_s[1]) * float(line_s[4])

    if 'Total' == line_s[0] and 'system' == line_s[1]:
        # print(line_s[0])
        # print(ite)
        # mass[ite] = mass_sum
        if ite == len(mass):
            mass.append(mass_sum)
        mass_sum = 0


else:
    # print(mass)
    # out.writelines(str(mass))
    for i, n in enumerate(mass):
        print >> out, "%d   %.3f" % (i, n / mass[0])
    print('write complete!')
    source.close()
    out.close()
