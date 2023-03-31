# -*- coding: UTF-8 -*-
from asyncio import sleep

import allure
import pytest

from PageObjects.login_page import LoginPage
from TestDatas import global_datas as gd
from TestDatas.login_datas import invalid_data


@allure.feature("登录")
class TestLogin:
    @allure.story('登录成功')
    @allure.title('账号密码正确')
    def test_login_success(self, driver):
        LoginPage(driver).login_success(*gd.user)

    @allure.story('登录失败')
    @pytest.mark.parametrize("case", invalid_data)
    def test_login_failed(self, case, driver):
        allure.dynamic.title(case["case_name"])
        LoginPage(driver).login_failed(case["username"], case["password"], case["expect"])


if __name__ == '__main__':
    pytest.main(['-s', __file__])
