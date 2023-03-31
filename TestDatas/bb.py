# -*- coding: UTF-8 -*-
import pickle
from time import sleep

import pytest
import requests
from selenium import webdriver

driver = webdriver.Edge()


def test_foo1():
    driver.get("http://tkproc.huatu.com/mk/#/login")
    driver.find_element('xpath', '//input[@type="text"]').send_keys('admin')
    driver.find_element('xpath', '//input[@type="password"]').send_keys('admin')
    driver.find_element('xpath', '//span[text()="登录"]/..').click()
    sleep(3)
    # pickle.dump(driver.get_cookies(), open("cookie.pkl", 'wb'))
    print(driver.title)


def test_foo3():
    cookies = pickle.load(open("cookie.pkl", 'rb'))
    print(cookies)
    print("清除cookies")
    driver.delete_all_cookies()
    print(driver.get_cookies())
    print("重新访问")
    driver.get("http://tkproc.huatu.com/mk/#/home/paper_list")
    driver.refresh()
    for i in cookies:
        driver.add_cookie(i)
    print("添加cookies")
    print(driver.get_cookies())
    sleep(3)
    print(driver.current_url)
    print("再次访问")
    driver.get("http://tkproc.huatu.com/mk/#/home/paper_list")

def foo2():
    url = "http://test-ns.htexam.com/ms-api/auth/login"
    data = {
        "username": "admin",
        "password": "admin"
    }
    req = requests.post(url, data=data)
    print(req.json()['data']['token'])


if __name__ == '__main__':
    test_foo1()
