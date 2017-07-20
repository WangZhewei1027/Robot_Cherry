# Robot_Cherry

## 项目介绍:</br>

这是一个基于个人微信平台的聊天机器人，将会拥有智能应答，语音识别，语音合成等无限可能！扫码登陆即可使用

> 使用Python3开发</br>
> itchat库</br>
> 百度语音识别接口</br>
> 图灵机器人接口</br>
> 平台：Windows10 64位；IDE：pycharm；MarkDown文档编辑：MarkDownPad 2；</br>

## 项目结构:</br>

- code	这是源代码目录
	- modules	这是各种模块的目录
		- *_init_.py* 设置脚本
		- *robot_port.py* 调用图灵机器人的模块
		- *phone.py* 查询手机号码归属地等的模块
	- *front.py* 与微信对接的前端，实际运行的也是这个脚本
	- *main.py* 主要处理对话的模块
- *.gitignore* 忽略文件表
- *init.py* 设置脚本
- *LICENSE*	协议
- *README.md*	这就是此文档

## 注意事项:</br>

1. 注意在提交项目时不要把*.pkl*文件提交了，那是登陆临时文件</br>
2. 程序中所有api key等仅供测试！实际使用请申请自己的api key</br>