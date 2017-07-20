# coding=utf-8
"""
这是查询手机归属地的模块
"""

from bs4 import BeautifulSoup
import requests


def check_phone(content):  # TODO：可能出现有间隔的两串数字，这种情况需要处理
    for i in range(0, len(content)):
        if content[i:i+11].isdigit():
            return content[i:i+11]


def ask_phone(p):  # 这个函数写的不好，不优美 TODO：重构此函数，输出结果去掉单引号
    url = 'http://www.ip138.com:8080/search.asp?mobile=%s&action=mobile' % p
    r = requests.get(url)
    r.encoding = 'GBK'
    soup = BeautifulSoup(r.text, "html.parser")
    i = 0
    list = {}
    for string in soup.stripped_strings:
        t = repr(string)
        if i == 8: list[0] = t
        if i == 13: list[1] = t
        if i == 15: list[2] = t
        if i == 17: list[3] = t
        if i == 19: list[4] = t
        i = i + 1
    str = '手机号：' + list[0] + '\n' + '归属地：' + list[1] + '\n' + '卡类型：' + list[2] + '\n' + '区号：' + list[3] + '\n' + '邮编：' + \
          list[4]
    return str
