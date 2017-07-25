# coding=utf-8
"""
这是调用图灵机器的模块，官网：http://www.tuling123.com/
"""


import urllib
from urllib import request
import json


def get_html(url):
    page = request.urlopen(url)
    html = page.read()
    return html


def robot_tuling(info):
    key = '2cd6a7c1b4b04e2a95e9f507fdedd923'  # 我的key仅供测试，实际使用时请申请自己的key（反正是免费的）
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    re = api + urllib.parse.quote(info)
    response = get_html(re).decode()
    dic_json = json.loads(response)
    return dic_json['text']  # 返回处理结果
