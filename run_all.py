#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/4 20:36 
# @Author : 墨
# @Version：V 0.1
# @File : run_all.py
# @desc :
import unittest
from unittestreport import TestRunner
from datetime import datetime
from conf import read_dir

# 获取当前时间
now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# suite = unittest.defaultTestLoader.discover(r'C:\Users\moster\Desktop\框架\testcases')
# 收集测试用例
suite = unittest.defaultTestLoader.discover(read_dir.test_cases_dir)
# 生成报告
runner = TestRunner(suite, filename=now_time + 'reports.html', tester='墨渊', report_dir='reports').run()
