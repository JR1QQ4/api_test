#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from configparser import ConfigParser


# # 1. 实例化
# conf = ConfigParser()
# # 2. 读取配置文件
# conf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "my.ini")
# conf.read(conf_path, encoding="utf-8")
# # 3. 获取
# name = conf.get('log', "name")
# level = conf.get('log', "level")
# file_name = conf.get('log', "file_name")
# section = conf.items('log')
# sections = conf.sections()
# print(name)
# print(level)
# print(file_name)
# print(section)
# print(sections)

class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super(HandleConfig, self).__init__()
        self.read(file_path, encoding="utf-8")


conf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "my.ini")
conf = HandleConfig(conf_path)

if __name__ == '__main__':
    print(conf.get('log', "name"))
