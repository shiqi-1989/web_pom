# -*- coding: UTF-8 -*-
import allure
from io import BytesIO

import pytesseract.pytesseract
from PIL import Image

from Common.keys_web import WebKeys
from TestDatas import global_datas as gd
from PageLocators import MBTI_page_locs as loc

from Common.my_logger import logger


class MbtiPage(WebKeys):
    @allure.step("打开MBTI页面")
    def open_url(self, url):
        self.open(url)
        self.wait(1)

    @allure.step("点击开始测试按钮")
    def click_start(self):
        self.click(loc.start_test, "首页-点击开始测试")
        self.wait(1)

    @allure.step("第 {question} 题点击选项：{option}")
    def click_options(self, question, option):
        print(question, option)
        location = loc.option_loc.copy()
        location[1] = location[1].replace('option', option)
        self.click(location, f"第{question}题-点击选项{option}", index=question - 1)
        self.wait(2)

    @allure.step("输入昵称 {nickname}")
    def enter_nickname(self, nickname):
        self.input(loc.nickname_loc, "提交结果页-输入昵称", nickname)
        self.wait(1)

    @allure.step("点击提交按钮")
    def click_submit(self):
        self.click(loc.submit_loc, "提交结果页-点击提交按钮")
        self.wait(1)

    @allure.step("断言结果:预期 - {expect}  实际 - {actual}")
    def assert_result(self, expect, actual):
        logger.info(f"预期 - {expect}  实际 - {actual}")
        assert expect in actual

    def get_result(self):
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        # 截图
        answer_img = im.crop((280, 220, 670, 400)).convert('L')
        result = pytesseract.image_to_string(answer_img, lang="chi_sim+eng", config="--psm 6").replace(" ", "")
        if result:
            return result
        else:
            return "未识别结果"

    # 答题流程
    def test_answer(self, options, nickname, answer):
        self.open_url(gd.mbtr_url)
        self.click_start()
        for i in range(0, 8):
            option = options[i]
            self.click_options(i + 1, option)
        self.enter_nickname(nickname)
        self.click_submit()
        result = self.get_result()
        self.assert_result(answer, result)
