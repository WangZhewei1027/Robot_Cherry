# coding=utf-8
"""
这是查询手机归属地的模块
"""

from bs4 import BeautifulSoup
import requests


def check_phone(content):  # 检查是否有电话号码

    for i in range(0, len(content)):
        if (content[i:i + 11].isdigit()) and (content[i] == '1'):  # TODO:解决不是合法手机号码也会被识别的bug
            return content[i:i + 11]


def ask_phone(p):  # 这个函数写的不好，不优美 TODO：重构此函数
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
    str = str.replace('\\xa0', ' ')  # 去除特殊符号
    str = str.replace("'", '')  # 去除单引号

    return str
