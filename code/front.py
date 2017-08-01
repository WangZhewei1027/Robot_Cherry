# coding=utf-8
"""
这是对微信的接口
运行的应该是此脚本！
关于itchat的资料：http://www.tuicool.com/articles/VJZRRfn ；GitHub：https://github.com/littlecodersh/ItChat
"""

import os
import random
import threading
import time

import itchat
from itchat.content import *

from code import main
from code.modules.voice import *

ROBOT_NAME = 'Cherry'  # **特别注意!**：请将ROBOT_NAME改为自己个人微信号的名字


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('我自动接受了你的好友请求，Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(RECORDING)
def recoding_reply(msg):
    api_key = "IfGaEWNp6MGpKHuGv0cRqmig"
    api_secert = "4077f676b0b342e841da655e07a8faa2"
    bdr = BaiduRest("test_python", api_key, api_secert)

    msg['Text'](msg['FileName'])

    f = msg['FileName'] + '.wav'
    os.system('ffmpeg -i ' + msg['FileName'] + ' -ac 1 -ar 8000 -vn ' + f)  # 使用ffmpeg把mp3转为wav
    content = bdr.get_text(msg['FileName'] + '.wav')

    os.remove(msg['FileName'])
    os.remove(f)

    return main.reply(content[0], msg['FromUserName'][3:len(msg['FromUserName']) - 10])


@itchat.msg_register(TEXT)
def text_reply(msg):
    content = msg['Text']
    fromUserName = msg['FromUserName']
    reply = main.reply(content, fromUserName[5:10])
    time.sleep(random.randint(0, len(content)))
    itchat.send(reply, toUserName=msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)  # 后注册的消息优于先注册的消息，在此先处理群聊消息，就不会出现冲突
def text_reply(msg):
    if msg['isAt']:  # 如果消息@自己才对消息做出反应

        fromUserName = msg['FromUserName']
        content = msg['Text']
        # 这里的content中包含'@...'
        content = content[0:content.find(ROBOT_NAME) - 1] + content[
                                                            msg['Text'].find(ROBOT_NAME) + len(ROBOT_NAME):len(content)]
        # 这句将content中'@...'去除了
        reply = main.reply(content, fromUserName[5:10])
        time.sleep(random.randint(0, len(reply)))
        itchat.send(u'@%s\u2005%s' % (msg['ActualNickName'], reply), fromUserName)
        # 这里的'@...'后面要加上'\u2005'这个Unicode字符，这样的@才是有效的


def birthday():  # TODO：重写函数 2017_07_27
    p = [['07', '00', '00', '早安', 1], ['12', '00', '00', '午好', 1], ['22', '00', '00', '晚安', 1]]

    class15ChatroomID = '@@988d6acddf9c8fa9fb97ed867e548633233b842a6602a11afc16728b672c697c'
    while (1):
        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        hour = time.strftime('%H', time.localtime(time.time()))
        min = time.strftime('%M', time.localtime(time.time()))
        second = time.strftime('%S', time.localtime(time.time()))

        if hour == '00':
            for i in range(0, len(p)):
                p[i][4] = 0

        for i in range(0, len(p)):
            if p[i][4] == 0:
                if (p[i][0] <= hour) and (p[i][1] <= min) and (p[i][2] <= second):  # TODO:解决运行速度和秒的判断边缘情况冲突
                    itchat.send(p[i][3], class15ChatroomID)
                    p[i][4] = 1


itchat.auto_login(hotReload=True)  # 增加'hotReload=True'支持热插拔，短时断线重连

thread1 = threading.Thread(target=itchat.run)
thread2 = threading.Thread(target=birthday)
thread1.start()
thread2.start()

itchat.dump_login_status()
