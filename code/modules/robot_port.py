# coding=utf-8
"""
这是调用图灵机器的模块，官网：http://www.tuling123.com/
"""

import requests
import json


def robot_tuling(info, userid):
    url = "http://www.tuling123.com/openapi/api"
    key = '2cd6a7c1b4b04e2a95e9f507fdedd923'
    parameters = {'key': key, 'info': info, 'userid': userid}
    r = requests.post(url, data=parameters)
    a = json.loads(r.text)
    return a['text']
