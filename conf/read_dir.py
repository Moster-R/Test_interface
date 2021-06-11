#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/5 10:46 
# @Author : 墨
# @Version：V 0.1
# @File : read_dir.py
# @desc :
import os

# 当前文件路径
curred = os.path.abspath(__file__)
# 当前文件所在目录
conf_dir = os.path.dirname(curred)
# 项目根目录
root_dir = os.path.dirname(conf_dir)

# data路径
data_dir = os.path.join(root_dir, 'data')
# excl文件路径
excl_dir = os.path.join(data_dir, 'info.xlsx')

# log路径
log_dir = os.path.join(root_dir, 'logs')

# test_cases路径
test_cases_dir = os.path.join(root_dir, 'testcases')

