#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/5 10:21 
# @Author : 墨
# @Version：V 0.1
# @File : login.py
# @desc :
def login(username=None, password=None):
    if username is None or password is None:
        return {"code": "400", "msg": "用户名或密码为空"}
    elif username == 'yuz' and password == '123':
        return {"code": "200", "msg": "登录成功"}
    return {"code": "300", "msg": "用户名或密码错误"}
