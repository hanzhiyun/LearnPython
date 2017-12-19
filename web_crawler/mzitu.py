#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-29 10:52:59
# @Author  : Han Zhiyun (hanzhiyun1995@foxmail.com)
# @Link    : http://example.org
# @Version : $Id$


# # 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
# all_url = 'http://www.mzitu.com/all'  # 开始的URL地址
# # 使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容
# # headers为上面设置的请求头、请务必参考requests官方文档解释
# start_html = requests.get(all_url, headers=headers)
# # print(start_html.text) ##打印出start_html
# # (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
# # 使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
# Soup = BeautifulSoup(start_html.text, 'lxml')
# # 使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
# # li_list = Soup.find_all('li')
# # for li in li_list:  # 这个不解释了。看不懂的小哥儿回去瞅瞅基础教程
# #     print(li)  # 同上
# all_a = Soup.find('div', class_='all').find_all('a')
# # 意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
# for a in all_a:
#     # print(a)
#     title = a.get_text()  # 取出a标签的文本
#     path = str(title).strip()
#     os.makedirs(os.path.join("G:\Pictures\mzitu", path))
#     os.chdir("G:\Pictures\mzitu\\" + path)
#     href = a['href']
#     # print(title, href)
#     html = requests.get(href, headers=headers)
#     html_Soup = BeautifulSoup(html.text, 'lxml')
#     max_span = html_Soup.find(
#         'div', class_='pagenavi').find_all('span')[-2].get_text()
#     for page in range(1, int(max_span) + 1):
#         page_url = href + '/' + str(page)
#         # print(page_url)
#         img_html = requests.get(page_url, headers=headers)
#         img_Soup = BeautifulSoup(img_html.text, 'lxml')
#         img_url = img_Soup.find('div', class_='main-image').find('img')['src']
#         # print(img_url)
#         name = img_url[-9:-4]
#         img = requests.get(img_url, headers=headers)
#         f = open(name + '.jpg', 'ab')
#         f.write(img.content)
#         f.close()


from bs4 import BeautifulSoup
import os
import io
import sys
from download import request


sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码


class mzitu():

    def all_url(self, url):
        html = request.get(url, 3)  # 这儿替换了，并加上timeout参数
        html_Soup = BeautifulSoup(html.text, 'lxml')
        all_a = html_Soup.find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)  # 加点提示不然太枯燥了
            # 我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            path = str(title).replace("?", '_')
            self.mkdir(path)  # 调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
            href = a['href']
            # 调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！
            self.html(href)

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("G:\Pictures\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("G:\Pictures\mzitu", path))
            os.chdir(os.path.join("G:\Pictures\mzitu", path))  # 切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            os.chdir(os.path.join("G:\Pictures\mzitu", path))  # 切换到目录
            return False

    def html(self, href):  # 这个函数是处理套图地址获得图片的页面地址
        html = request.get(href, 3)  # 这儿更改了一下（是不是发现  self 没见了？）
        max_span = BeautifulSoup(html.text, 'lxml').find(
            'div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  # 调用img函数

    def img(self, page_url):  # 这个函数处理图片页面地址获得图片的实际地址
        img_html = request.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find(
            'div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):  # 这个函数保存图片
        name = img_url[-9:-4]
        img = request.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    # def request(self, url):
    #     headers = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    #     content = requests.get(url, headers=headers)
    #     return content


Mzitu = mzitu()  # 实例化
Mzitu.all_url('http://www.mzitu.com/all')  # 给函数all_url传入参数  你可以当作启动爬虫（就是入口）
