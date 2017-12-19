#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-29 19:48:31
# @Author  : Han Zhiyun (hanzhiyun1995@foxmail.com)
# @Link    : http://example.org
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import os

# 爬取目标
url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = "G:\Pictures\mzitu\\"
# 设置报头，Http协议
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
          'Referer':'http://www.mzitu.com/'}

# driver = webdriver.PhantomJS(executable_path='D:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs')
# driver.get(url)
# driver.implicitly_wait(1)
# print(driver.get_cookies())
# cookies = driver.get_cookies()
# 爬取的预览页面数量
preview_page_cnt = 4
for cur_page in range(1, int(preview_page_cnt) + 1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers=header)
    # 解析网页
    soup = BeautifulSoup(cur_page.text, parser)
    # 图片入口和文字入口取一个即可
    preview_link_list = soup.find(id='pins').find_all(
        'a', target='_blank')[1::2]
    for link in preview_link_list:
        dir_name = link.get_text().strip().replace('?', '')
        link = link['href']
        soup = BeautifulSoup(requests.get(
            link, headers=header).text, parser)
        # 获取图片数量
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[
            4].get_text()
        # 创建目录
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print('directory exist!')
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)  # 进入目录，开始下载
        print('下载 ' + dir_name + '...')
        # 遍历获取每页图片的地址
        for pic_index in range(1, int(pic_cnt) + 1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers=header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src']
            # pic_src = pic_src.replace('http', 'https')
            pic_name = pic_src.split('/')[-1]
            f = open(pic_name, 'wb')
            f.write(requests.get(pic_src, headers=header).content)
            f.close()
            # os.system('you-get -O ' + pic_name + ' ' + pic_src)
        os.chdir(cur_path)  # 完成下载，退出目录
print('下载完成')
