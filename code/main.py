# coding=utf-8
"""
这是主要处理文字内容的模块
"""

from code.modules.phone import *
from code.modules.robot_port import robot_tuling


def process(content):  # 在这个函数中编写自定义应答模式，优先级高于调用图灵机器人

    phone_num = check_phone(content)  # 检查文字中是否包含电话号码
    if phone_num:  # 如果包含电话号码，则返回归属地等信息
        return ask_phone(phone_num)


def donnotkown(content):
    return robot_tuling(content)


def reply(content):  # 若使用了自定义应答，则返回应答，反则调用图灵机器人，并返回应答
    answer = process(content)
    if answer is None:
        return donnotkown(content)
    else:
        return answer
