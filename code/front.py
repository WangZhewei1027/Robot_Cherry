# coding=utf-8
"""
这是对微信的接口
运行的应该是此脚本！
关于itchat的资料：http://www.tuicool.com/articles/VJZRRfn ；GitHub：https://github.com/littlecodersh/ItChat
"""


import itchat
from itchat.content import *
from code import main


ROBOT_NAME = '机器人cherry'  # **特别注意!**：请将ROBOT_NAME改为自己个人微信号的名字


@itchat.msg_register(TEXT)
def text_reply(msg):
    content = msg['Text']
    itchat.send(main.reply(content), toUserName=msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)  # 后注册的消息优于先注册的消息，在此先处理群聊消息，就不会出现冲突
def text_reply(msg):
    if msg['isAt']:  # 如果消息@自己才对消息做出反应
        content = msg['Text']
        # 这里的content中包含'@...'
        content = content[0:content.find(ROBOT_NAME)-1]+content[msg['Text'].find(ROBOT_NAME) + len(ROBOT_NAME):len(content)]
        # 这句将content中'@...'去除了
        itchat.send(u'@%s\u2005%s' % (msg['ActualNickName'], main.reply(content)), msg['FromUserName'])
        # 这里的'@...'后面要加上'\u2005'这个Unicode字符，这样的@才是有效的

itchat.auto_login(hotReload=True)  # 增加'hotReload=True'支持热插拔，短时断线重连
itchat.run()
itchat.dump_login_status()
