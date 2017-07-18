# coding=utf-8
"""
这是主要处理文字内容的模块
"""


from robot_port import robot_tuling


def process(a):  # 在这个函数中编写自定义应答模式，优先级高于调用图灵机器人
    return None


def donnotkown(a):
    return robot_tuling(a)


def reply(a):  # 若使用了自定义应答，则返回应答，反则调用图灵机器人，并返回应答
    answer = process(a)
    if answer == None:
        return donnotkown(a)
    else:
        return answer
