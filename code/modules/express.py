# coding=utf-8
"""
查询快递模块
"""

import urllib.request as ure
import json


def check_express(content):
    for i in range(0, len(content)):
        if content[i].isdigit():
            for j in range(i + 1, len(content)+1):
                if not content[i:j].isdigit():
                    return content[i:j-1]
                if j == len(content):
                    return content[i:j]


def search_express(num):
    url1 = "http://www.kuaidi100.com/autonumber/autoComNum?text=" + num
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    req = ure.Request(url1, headers=head)
    response = ure.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    auto = target['auto']
    if len(auto) < 1:
        return "你输入的快递单号不存在！"

    # 快递公司
    comCode = target['auto'][0]['comCode']

    # 根据快递单号和所属的快递公司进行查询快递详细信息
    url2 = "http://www.kuaidi100.com/query?"
    url2 += 'type=' + comCode + '&postid=' + num + '&id=1&valicode=&temp=0.8810472078621387'
    req = ure.Request(url2, headers=head)
    response = ure.urlopen(req)

    html = response.read().decode('utf-8')
    target = json.loads(html)

    try:
        info = target['data']

        # print("你的快递所属的公司是：", comCode) TODO:目前大多数情况下无法正常显示快递公司 2017_07_22
        str = ''
        for eachData in info:
            str = str + (eachData['context'] + ',' + eachData['time'] + '---' + eachData['ftime']) + '\n'
        if str == '':
            return "你输入的快递单号不存在或已过期！"
        else:
            return "你的快递信息如下：\n"+str
        return str
    except KeyError as reason:
        print(target['message'])
