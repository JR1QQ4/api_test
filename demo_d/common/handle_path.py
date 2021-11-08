#!/usr/bin/python
# -*- coding:utf-8 -*-
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'datas')
CONF_DIR = os.path.join(BASE_DIR, 'conf')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
CASE_DIR = os.path.join(BASE_DIR, 'testcases')


if __name__ == '__main__':
    print(BASE_DIR)
    print(DATA_DIR)
    print(CONF_DIR)
    print(LOG_DIR)
    print(REPORT_DIR)
    print(CASE_DIR)


