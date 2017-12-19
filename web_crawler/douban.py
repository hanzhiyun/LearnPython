#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-29 20:32:20
# @Author  : Han Zhiyun (hanzhiyun1995@foxmail.com)
# @Link    : http://example.org
# @Version : $Id$

import requests
import re
import time
from bs4 import BeautifulSoup
'''
2 ＝ 大胸妹
3 ＝ 美腿控
4 ＝ 有颜值
5 ＝ 大杂烩
6 ＝ 小翘臀
'''
cat = '2'
img = 'http://www.dbmeinv.com/dbgroup/show.htm?cid=' + cat
end = '/dbgroup/show.htm?cid=' + cat + '&pager_offset=100'
urls = []


def getURLs(mainURL):
    time.sleep(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    html = requests.get(mainURL).text
    soup = BeautifulSoup(html, 'html.parser')
    picURL = re.findall('<img class.*?src="(.+?\.jpg)"', html, re.S)
    for url in picURL:
        url = re.sub('bmiddle', 'large', url, 1)
        url = re.sub('https', 'http', url, 1)
        urls.append(url)
        print(url)
    asoup = soup.select('.next a')[0]['href']
    Next_page = 'http://www.dbmeinv.com' + asoup
    if asoup != end:
        getURLs(Next_page)
    else:
        print('链接已处理完毕！')
    return urls


url = getURLs(img)
i = 0
for each in url:
    pic = requests.get(each, timeout=10)
    picName = 'G:\Pictures\douban\\' + str(i) + '.jpg'
    fp = open(picName, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

print('图片下载完成')
