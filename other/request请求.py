#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/7 21:28
# @Author : 墨
# @Version：V 0.1
# @File : requset_flask.py
# @desc :

import requests
import pprint
import unittest


class TestRegister(unittest.TestCase):

    def test_01(self):
        url = "http://api.lemonban.com/futureloan/member/login"
        headers = {"Content-Type": "application/json", "X-Lemonban-Media-Type": "lemonban.v2"}
        data = {"mobile_phone": "18478048477", "pwd": "130658ct"}

        response = requests.request(method='post', headers=headers, url=url, json=data)
        response.json().get('msg')
        print(response)


