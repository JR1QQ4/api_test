#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from configparser import ConfigParser

from handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, conf_file):
        super(Config, self).__init__()
        self.read(conf_file)


conf = Config(os.path.join(CONF_DIR, 'conf.ini'))
