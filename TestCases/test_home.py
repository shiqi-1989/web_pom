# -*- coding: UTF-8 -*-
import allure
import pytest

from PageObjects.home_page import HomePage


@allure.feature("主页")
class TestHome:
    @allure.story("退出登录")
    def test_logout(self, login, ):
        HomePage(login).logout()


if __name__ == '__main__':
    # pytest.main(['-sv', '--workers=1', '--tests-per-worker=3', __file__])
    pytest.main(['-s', __file__])
