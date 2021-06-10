#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/5 9:51 
# @Author : 墨
# @Version：V 0.1
# @File : test_login.py
# @desc :
import unittest
from common.ExclHandler import ExclHandler
from unittestreport import ddt, list_data
import os
from login import login
from common.Logger import Log
from conf import read_dir


@ddt
class TestLogin(unittest.TestCase):
    dir_url = read_dir.excl_dir
    login_data = ExclHandler(dir_url, 'login').ReadExcl()
    log = Log().Logger

    @list_data(login_data)
    def test_login(self, data_info):
        """
        :param data_info:
        :return:
        """

        # 获取excl中data数据
        user_info = eval(data_info['data'])
        # 用户名
        username = user_info['username']
        # 密码
        password = user_info['password']
        # 预期结果
        expected = eval(data_info['expected'])
        assault = login(username, password)
        try:
            self.assertEqual(assault, expected)
            self.log.info("用例执行成功")
        except AssertionError:
            self.log.error("用例执行失败")
