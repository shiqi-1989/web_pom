# -*- coding: UTF-8 -*-
from configparser import ConfigParser
import os

from Common.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(conf_dir, "logger.ini")
conf = HandleConfig(file_path)

# if __name__ == '__main__':
#     conf = HandleConfig("logger.ini")
#     conf.get("log","name")
