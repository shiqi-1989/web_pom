# -*- coding: UTF-8 -*-
from asyncio import sleep

import allure
import pytest

from PageObjects.MBTI_page import MbtiPage
from TestDatas.Mbti_datas import questions_data, questions_data_all, questions_data2


@allure.epic("MBTIui自动化测试")
# @allure.feature("MBTI测试")
class TestMbti:
    @allure.story('MBTI用例')
    @pytest.mark.parametrize("case", questions_data2)
    def test_mbti(self, case, driver):
        allure.dynamic.title(case["昵称"] + "__" + case["答案"])
        options = eval(case['选项'])
        MbtiPage(driver).test_answer(options, case["昵称"], case["答案"])


if __name__ == '__main__':
    from Common.handle_path import *
    import os

    pytest.main(['-s', __file__])
    os.system(f'allure generate {reports_temp_dir} -o {reports_html_dir} --clean')
