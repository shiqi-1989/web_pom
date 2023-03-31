import time
from io import BytesIO

from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
mobile_emulation = {"deviceName": "iPhone 6/7/8"}
# # 浏览器最大化
# edge_options.add_argument("--start-maximized")
edge_options.add_argument('--window-size=414,896')
# # 隐藏正受到自动测试软件的控制。
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# # 配置手机模式
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)
_driver = webdriver.Edge(options=edge_options)
_driver.get('http://mbti.360career.cn/workTest.html')
png = _driver.get_screenshot_as_png()
# 使用PIL库在内存中打开图像
im = Image.open(BytesIO(png))
# im = im.crop((left, top, right, bottom))
im = im.crop((0, 100, 400, 200))
result = pytesseract.image_to_string(im, lang="chi_sim")
print(result)
# 截图
im.save('截图.png')
im.show()
_driver.quit()