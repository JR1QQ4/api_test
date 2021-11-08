#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os

from handle_conf import conf
from handle_path import LOG_DIR


def create_log(name='MyLog', level='DEBUG0', filename='log.log', sh_level='DEBUG', fh_level='DEBUG'):
    log = logging.getLogger(name)
    log.setLevel(level)

    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)

    formats = '%(asctime)s - [%(filename)s--line:%(lineno)d>] - %(levelname)s: %(message)s'
    log_format = logging.Formatter(formats)
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    return log


my_log = create_log(
    name=conf.get('logging', 'name'),
    level=conf.get('logging', 'level'),
    filename=os.path.join(LOG_DIR, conf.get('logging', 'filename')),
    sh_level=conf.get('logging', 'sh_level'),
    fh_level=conf.get('logging', 'fh_level')
)
