# -*- coding: UTF-8 -*-
# 登录无效数据
invalid_data = [
    {"case_name": "账号错误", "username": "123", "password": "admin", "expect": "用户名不存在或密码错误"},
    {"case_name": "密码错误", "username": "admin", "password": "123", "expect": "用户名不存在或密码错误"},
    {"case_name": "账号为空", "username": "", "password": "123", "expect": "请输入用户名"},
]
