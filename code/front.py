# coding=utf-8
"""
这是对微信的接口
运行的应该是此脚本！
关于itchat的资料：http://www.tuicool.com/articles/VJZRRfn ；GitHub：https://github.com/littlecodersh/ItChat
"""

import itchat
import os
from itchat.content import *
from code import main
from code.modules.voice import *
import threading
import time

ROBOT_NAME = '机器人cherry'  # **特别注意!**：请将ROBOT_NAME改为自己个人微信号的名字


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(RECORDING)
def recoding_reply(msg):
    print(itchat.search_friends(name='仿佛从前（游戏）'))
    api_key = "IfGaEWNp6MGpKHuGv0cRqmig"
    api_secert = "4077f676b0b342e841da655e07a8faa2"
    bdr = BaiduRest("test_python", api_key, api_secert)

    msg['Text'](msg['FileName'])

    f = msg['FileName'] + '.wav'
    os.system('ffmpeg -i ' + msg['FileName'] + ' -ac 1 -ar 8000 -vn ' + f)  # 使用ffmpeg把mp3转为wav
    content = bdr.get_text(msg['FileName'] + '.wav')

    os.remove(msg['FileName'])
    os.remove(f)

    return main.reply(content[0])


@itchat.msg_register(TEXT)
def text_reply(msg):
    content = msg['Text']
    itchat.send(main.reply(content), toUserName=msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)  # 后注册的消息优于先注册的消息，在此先处理群聊消息，就不会出现冲突
def text_reply(msg):
    if msg['isAt']:  # 如果消息@自己才对消息做出反应
        content = msg['Text']
        # 这里的content中包含'@...'
        content = content[0:content.find(ROBOT_NAME) - 1] + content[
                                                            msg['Text'].find(ROBOT_NAME) + len(ROBOT_NAME):len(content)]
        # 这句将content中'@...'去除了
        itchat.send(u'@%s\u2005%s' % (msg['ActualNickName'], main.reply(content)), msg['FromUserName'])
        # 这里的'@...'后面要加上'\u2005'这个Unicode字符，这样的@才是有效的


def test():
    global p
    p = 0
    while (1):
        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        hour = time.strftime('%H', time.localtime(time.time()))
        min = time.strftime('%M', time.localtime(time.time()))
        second = time.strftime('%S', time.localtime(time.time()))

        if ((month == '07') and (day == '26')):
            if p == 0:
                itchat.send('祝徐玲同学生日快乐~【来自机器人cherry】', itchat.search_friends(name='青鲤鲤鲤鲤子')[0]['UserName'])
                p = 1
        time.sleep(10)


itchat.auto_login(hotReload=True)  # 增加'hotReload=True'支持热插拔，短时断线重连

threading._start_new_thread(test, ())
itchat.run()

itchat.dump_login_status()
