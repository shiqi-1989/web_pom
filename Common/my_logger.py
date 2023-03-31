# -*- coding: UTF-8 -*-

import logging
from Common.handle_path import logs_dir

name = "py30"
level = "DEBUG"
file_ok = True
file_name = "log.log"


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(name, level)
        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)
        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        # self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8", mode='w+')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if file_ok:
    file_name = logs_dir / file_name
else:
    file_name = None

logger = MyLogger(file_name)


if __name__ == '__main__':
    logger.info("1111111111111111")
    logger.warning("1111111111111111")
