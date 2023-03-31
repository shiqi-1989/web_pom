import time

from selenium import webdriver

edge_options = webdriver.EdgeOptions()
# edge_options.add_argument('--headless')
driver = webdriver.Edge(options=edge_options)
cookies = {
    'name': "_const_huatu_jsession_id_",
    'value': "1672453988640.a4e05a9d-8c94-4f4a-a2c0-c1cf7fbc807b.tiku.htexam.com/frontEnd"
}
edge_options.add_argument(
    'Cookie=_const_huatu_jsession_id_=1672453988640.a4e05a9d-8c94-4f4a-a2c0-c1cf7fbc807b.tiku.htexam.com/frontEnd')
driver.get("https://tiku.htexam.com/frontEnd/#/home/freeBuild")
lis = driver.find_elements("xpath", '//*/ul/li')

print(len(lis))

for i in range(len(lis)):
    print(f"第{i}个链接")
    lis = driver.find_elements("xpath", '//*/ul/li')
    name = lis[i].text
    try:
        lis[i].click()
    except:
        pass
    print(f"{name}: {driver.current_url}")
    driver.get("https://v.huatu.com/")
    time.sleep(3)
