#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from datetime import datetime
__author__ = 'Hanzhiyun'

pwd = os.getcwd()

print("Last Modified               Size\Byte  Name")
print('----------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '<DIR>' if os.path.isdir(f) else '     '
    print("%s   %s %12d  %s" % (mtime, flag, fsize, f))

os.system('pause')
