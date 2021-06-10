#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/7 21:28 
# @Author : 墨
# @Version：V 0.1
# @File : requset_flask.py
# @desc :
from flask import Flask

app = Flask(__name__)


@app.route('/login')
def login():
    return {"msg": "success", "data": "login ok", "code": "3306"}, {"set-cookie": "mo"}


app.run(debug=True)
