#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

# 项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# api 目录
api_dir = os.path.join(base_dir, "api")

# conf 目录
conf_dir = os.path.join(base_dir, "conf")

# data 目录
data_dir = os.path.join(base_dir, "data")

# out 目录
out_dir = os.path.join(base_dir, "out")
log_dir = os.path.join(base_dir, "out", "log")

# test_case 目录
case_dir = os.path.join(base_dir, "test_case")

# util 目录
util_dir = os.path.join(base_dir, "util")
