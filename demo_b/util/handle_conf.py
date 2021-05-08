#!/usr/bin/python
# -*- coding:utf-8 -*-
from configparser import ConfigParser, DuplicateSectionError


class HandleConf:
    all_data = []

    def __init__(self, file_path):
        self.conf = ConfigParser()
        self.file_path = file_path
        self.conf.read(file_path, encoding='utf-8')

    def get_all_conf(self):
        sections = self.conf.sections()
        for section in sections:
            section_dict = {}
            option_dict = {}
            options = self.conf.options(section)
            for option in options:
                option_dict[option] = self.conf.get(section, option)
            section_dict[section] = option_dict
            self.all_data.append(section_dict)
        return self.all_data

    def get_value(self, section, option):
        """
        获取配置文件中指定的值
        :param section: 配置选项
        :param option: 配置类型
        :return: 配置值
        """
        return self.conf.get(section, option)

    def set_value(self, section, option, value):
        self.conf.set(section, option, value)
        self.conf.write(open(self.file_path, 'w', encoding='utf-8'))

    def add_section(self, section, **kwargs):
        try:
            self.conf.add_section(section)
            for k, v in kwargs.items():
                self.set_value(section, k, v)
            else:
                self.conf.write(open(self.file_path, 'w', encoding='utf-8'))
        except DuplicateSectionError:
            print("Section【{}】已经存在，不能重复创建".format(section))

    def has_section(self):
        sections = self.conf.sections()


if __name__ == '__main__':
    from demo_b.util.handle_path import conf_dir
    import os

    log_conf = os.path.join(conf_dir, 'log.ini')
    print(log_conf)
    hc = HandleConf(log_conf)
    res = hc.get_all_conf()
    print(res)
    hc.add_section("log_log", a='b', c='d')
    # hc.add_section(log_conf, "log_log")

