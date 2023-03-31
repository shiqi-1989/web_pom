# -*- coding: UTF-8 -*-

# 开始测试按钮
start_test = ["XPATH", "//*[@id='button']"]

# 选项
option_loc = ["XPATH", "//*[@class='choice']/span[contains(text(),'option')]"]
option_loc_A = ["XPATH", "//*[@class='choice']/span[contains(text(),'A')]"]
option_loc_B = ["XPATH", "//*[@class='choice']/span[contains(text(),'B')]"]

# 昵称输入款
nickname_loc = ["XPATH", "//input[@placeholder='输入你的昵称']"]

# 提交按钮
submit_loc = ["XPATH", '//div[@class="subBtn"]']


if __name__ == '__main__':
    loc = option_loc[1]
    num = "1"
    option = 'A'
    aa = loc.replace('option', option).replace('question', num)
    print(aa)