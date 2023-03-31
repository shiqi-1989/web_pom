# -*- coding: UTF-8 -*-
from urllib.parse import urljoin

# 基础域名
base_url = "http://tkproc.huatu.com"
# 登录地址
# login_url = "http://127.0.0.1:8866/accounts/login/"
login_url = "http://10.1.48.20:3000/"

mbtr_url = "http://mbti.360career.cn/workTest.html"
# 主页
home_url = urljoin(base_url, '/mk/#/home')
# 用户 (用户名、密码)
user = ("admin", "admin")