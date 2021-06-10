#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/28 20:33 
# @Author : 墨
# @Version：V 0.1
# @File : data_separation.py
# @desc :

import yaml


def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = yaml.safe_load(fp)
        return data


if __name__ == '__main__':
    res = read_yaml(r'D:\Program Files\Lemon\fnc\interface\data.yaml')
    print(res)
