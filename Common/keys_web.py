# -*- coding: UTF-8 -*-
"""
封装关键字驱动
结构中属于行为代码层
主要作为一个工具类角色
包含常规的操作行为：
如：
输入、点击、切换标签页
"""
import time
from ast import literal_eval

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Common.my_logger import logger


class WebKeys:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 定位元素
    def locator(self, loc, page_action, index=0):
        logger.info(f"在行为：{page_action}，定位元素：{loc}")
        try:
            el = self.driver.find_elements(getattr(By, loc[0]), loc[1])[index]
            self.driver.execute_script("arguments[0].scrollIntoView(false);", el)
            self.highlight(el)
        except Exception as e:
            logger.exception(f"{page_action}-定位元素失败！")
            raise
        else:
            return el

    # 等待元素可见
    def wait_visible(self, loc, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素可见
        :param loc:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info(f"在行为：{page_action},等待元素可见：{loc}")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((getattr(By, loc[0]), loc[1])))
        except Exception as e:
            logger.exception(f"{page_action}-等待元素可见失败！")
            raise
        else:
            end = time.time()
            logger.info(f"等待元素耗时：{(end - start)}")

    # 等待元素可点击
    def wait_clickable(self, loc, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素可点击
        :param loc:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info(f"在行为：{page_action},等待元素可点击：{loc}")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable((getattr(By, loc[0]), loc[1])))
        except Exception as e:
            logger.exception(f"{page_action}-等待元素可点击失败！")
            raise
        else:
            end = time.time()
            logger.info(f"等待元素耗时：{(end - start)}")

    # 等待元素存在
    def wait_presence(self, loc, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素存在
        :param loc:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info(f"在行为：{page_action},等待元素存在：{loc}")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located((getattr(By, loc[0]), loc[1])))
        except Exception as e:
            logger.exception(f"{page_action}-等待元素存在失败！")
            raise
        else:
            end = time.time()
            logger.info(f"等待元素耗时：{(end - start)}")

    # 聚焦元素并高亮显示
    def highlight(self, el):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            el,
            "border: 3px solid red"
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            el,
            "border: 2px solid blue"
        )
        time.sleep(0.3)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            el,
            ""
        )

    # 访问url
    # def open(self, url):
    #     self.driver.get(url)
    def open(self, url):
        self.driver.get(url)

    # 等待
    def wait(self, time_):
        time.sleep(time_)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 关闭当前标签页
    def close(self):
        self.driver.close()

    # 输入内容
    def input(self, loc, page_action, value, timeout=20, poll_frequency=0.5, index=0):
        # self.wait_clickable(loc, page_action, timeout, poll_frequency)
        el = self.locator(loc, page_action, index)
        logger.info(f"在行为：{page_action}，给元素：{loc} 输入文本值：{value}")
        try:
            el.clear()
            el.send_keys(value)
        except Exception as e:
            logger.exception("元素输入文本失败!")
            raise

    # 点击（左击）
    def click(self, loc, page_action, timeout=20, poll_frequency=0.5, index=0):
        # self.wait_clickable(loc, page_action, timeout, poll_frequency)
        el = self.locator(loc, page_action, index)
        logger.info(f"在行为：{page_action}，点击元素：{loc}")
        try:
            try:
                el.click()
            except:
                self.driver.execute_script("arguments[0].click();", el)
        except Exception as e:
            logger.exception("点击元素失败！")
            raise
        # self.driver.execute_script("arguments[0].click();", el)

    # 切换窗口 handles
    def switch_window(self, num):
        time.sleep(1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[num])
        return self

    # 获取页面title
    def get_tilte(self):
        return self.driver.title

    # 获取页面文本
    def get_text(self, loc, page_action, timeout=20, poll_frequency=0.5):
        self.wait_presence(loc, page_action, timeout, poll_frequency)
        el = self.locator(loc, page_action)
        logger.info(f"在行为：{page_action}，获取元素 {loc} 的文本值。")
        try:
            txt = el.text
        except Exception as e:
            logger.exception("获取元素文本失败！")
        else:
            logger.info(f"文本值为：{txt}")
            return txt

    # 获取页面链接
    def current_url(self):
        return self.driver.current_url

    # 刷新当前页面
    def refresh_page(self):
        logger.info("刷新当前页面")
        self.driver.refresh()
        return self

    # 回退到上一页
    def back_to_previous(self):
        logger.info("回退到上一页")
        self.driver.back()
        return self

    # 前进到下一页
    def forward_to_next(self):
        logger.info("前进到下一页")
        self.driver.forward()
        return self

    # 断言元素是否存在
    def isElementExist(self, loc, page_action, value=None, timeout=20, poll_frequency=0.5):
        logger.info(f"在行为：{page_action}，判断 {loc} 是否存在。")
        try:
            loc = self.loc_format(loc, value)
            self.wait_visible(loc, page_action, timeout, poll_frequency)
            self.locator(loc, page_action)
        except:
            logger.exception(f"{loc}元素不存在!")
            return False
        else:
            logger.info("元素存在!")
            return True

    # 截图
    def get_img(self, page_action="成功截图"):
        with allure.step('添加截图...'):
            allure.attach(self.driver.get_screenshot_as_png(), page_action, allure.attachment_type.PNG, '.png')
        # base_dir = Path(__file__).resolve().parent.parent
        # img_time = time.strftime("%Y_%m_%d_%H_%M_%S_", time.localtime())
        # file_path = f"{base_dir}/img/{txt}.png"
        # self.driver.save_screenshot(file_path)

    # 元素格式化
    def loc_format(self, loc, args):
        loc[1] = loc[1].format(args)
        return loc


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    bas = WebKeys(driver)
    bas.open("https://www.baidu.com/")

    loc = ['id', 'kw']
    bas.input(loc, '输入', '111')
    loc_btn = ['id', 'su']
    bas.click(loc_btn, '点击')
    bas.locator(['xpath', '//a[contains(text(),"下一页")]/..'], '定位下一页')
