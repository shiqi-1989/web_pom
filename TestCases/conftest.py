# 写在conftest.py

import os
import allure
from selenium import webdriver
import pytest
from filelock import FileLock

from Common.my_logger import logger
from PageObjects.login_page import LoginPage
from TestDatas import global_datas as g_data

_driver = None


# 添加报错截图到allure报告里
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    hook pytest失败
    :param item:
    :param call:
    :return:
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    # if rep.when == "call" and rep.failed:
    #     mode = "a" if os.path.exists("../failures") else "w"
    #     with open("../failures", mode) as f:
    #         # let's also access a fixture for the fun of it
    #         if "tmpdir" in item.fixturenames:
    #             extra = " (%s)" % item.funcargs["tmpdir"]
    #         else:
    #             extra = ""
    #         f.write(rep.nodeid + extra + "\n")
    #     # pic_info = adb_screen_shot()
    #     with allure.step('添加失败截图...'):
    #         allure.attach(_driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG, '.png')

    if rep.when == "call":
        if rep.failed:
            with allure.step('用例失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), 'FAILED截图', allure.attachment_type.PNG, '.png')
        if rep.passed:
            with allure.step('用例成功截图...'):
                allure.attach(_driver.get_screenshot_as_png(), 'PASSED截图', allure.attachment_type.PNG, '.png')


@pytest.fixture(scope='session', autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
    # # 浏览器最大化
    # options.add_argument("--start-maximized")
    options.add_argument('--window-size=414,896')
    # # 隐藏正受到自动测试软件的控制。
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # # 配置手机模式
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    logger.info("========== session级 前置操作:打开浏览器 ==========")
    global _driver
    with allure.step("session级 前置操作:打开浏览器"):
        # 进程锁
        with FileLock("session.lock"):
            if _driver is None:
                _driver = webdriver.Chrome(options=options)
                # _driver = webdriver.Edge(options=options)
                # _driver.maximize_window()
    yield _driver
    logger.info("========== session级 后置操作:关闭浏览器,退出会话 ==========")
    with allure.step("session级 后置操作:关闭浏览器,退出会话"):
        _driver.quit()


@pytest.fixture(scope="session")
def login(driver):
    logger.info("========== class级 前置操作:登录 ===============")
    with allure.step("class级 前置操作:登录"):
        # 进程锁
        with FileLock("class.lock"):
            LoginPage(driver).login_success(*g_data.user)
    yield driver


@pytest.fixture()
def home(login):
    logger.info("========== function级 前置操作: 回到主页 ===============")
    with allure.step("function级 前置操作:回到主页"):
        login.get(g_data.home_url)
    yield login
