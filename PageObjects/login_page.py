# -*- coding: UTF-8 -*-
import allure

from Common.keys_web import WebKeys
from TestDatas import global_datas as gd
from PageLocators import MBTI_page_locs as loc


class LoginPage(WebKeys):
    @allure.step("打开登录页")
    def open_url(self, url):
        self.open(url)
        self.wait(1)

    @allure.step("点击页面动画")
    def click_canvas(self):
        self.click(loc.canvas_loc, "登录-点击动画")
        self.wait(1)

    @allure.step("输入用户名")
    def enter_username(self, username):
        self.input(loc.username_el, "登录-输入用户名", username)

    @allure.step("输入密码")
    def enter_password(self, password):
        self.input(loc.password_el, "登录-输入密码", password)

    @allure.step("点击登录按钮")
    def click_login(self):
        self.click(loc.login_btn_el, "登录-点击登录按钮")

    @allure.step("获取失败弹框内容")
    def get_login_fail_msg(self):
        """
        获取登录失败时，alert提示框内容。
        :return:
        """
        msg = self.get_text(loc.login_failed_popup_lod, "登录-获取失败信息")
        return msg

    # 正常登录
    def login(self, username, password):
        self.open_url(gd.login_url)
        self.click_canvas()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def login_success(self, username, password):
        self.login(username, password)
        assert self.isElementExist(loc.home_title_loc, "登录成功")

    # 异常登录
    def login_failed(self, username, password, expect):
        self.login(username, password)
        assert expect == self.get_login_fail_msg()
