#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/28 19:56
# @Author : 墨
# @Version：V 0.1
# @File : ExclHandler.py
# @desc :
import openpyxl
import os
from conf import read_dir


class ExclHandler:

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.workbook = openpyxl.load_workbook(file_name)
        self.sheet = self.workbook[sheet_name]

    def ReadExcl(self):
        # 取出sheet里的值转化成列表
        value = list(self.sheet.values)
        # 取标题
        title = value[0]
        # 取单元格的值
        rows = value[1:]
        new_dict = [dict(zip(title, row)) for row in rows]
        return new_dict


if __name__ == '__main__':
    my_list = []
    dir_url = os.path.join(read_dir.excl_dir)
    ex = ExclHandler(dir_url, 'login')
    data_info = ex.ReadExcl()
    # print(data_info)
    for user_info in data_info:
        # print(user_info)
        data_Json = eval(user_info['data'])
        username = data_Json['username']
        password = data_Json['password']
        expected = eval(user_info['expected'])
        print(username, password, expected)
