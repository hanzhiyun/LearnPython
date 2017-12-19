#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import requests
from bs4 import BeautifulSoup

proxy_url = 'http://www.kuaidaili.com/ops/'
iplist = [] ##初始化一个list用来存放我们获取到的IP
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
content = requests.get(proxy_url, headers=headers) ##不解释咯
for tag in BeautifulSoup(content.text, 'lxml').find_all(attrs={'data-title': 'IP'}):
	iplist.append(tag.string.strip())
print(iplist)
