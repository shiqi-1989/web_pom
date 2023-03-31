# -*- coding: UTF-8 -*-
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
print(base_dir)

# 测试用例路径
cases_dir = Path.joinpath(base_dir, "TestCases")
# 测试用例调试路径
debug_dir = Path.joinpath(base_dir, "TestDebug")
# 测试数据的路径
datas_dir = Path.joinpath(base_dir, "TestDatas")
# 测试报告
reports_html_dir = Path.joinpath(base_dir, "Outputs", "reports")
reports_temp_dir = Path.joinpath(base_dir, "Outputs", "temp")
# 日志的路径
logs_dir = Path.joinpath(base_dir, "Outputs", "logs")
# 配置文件路径
conf_dir = Path.joinpath(base_dir, "Conf")
