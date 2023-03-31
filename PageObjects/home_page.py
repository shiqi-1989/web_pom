# -*- coding: UTF-8 -*-
import allure

from Common.keys_web import WebKeys
from PageLocators import home_page_locs as loc


class HomePage(WebKeys):

    @allure.step("点击退出系统")
    def logout(self):
        self.click(loc.logout_loc, "首页-退出登录")