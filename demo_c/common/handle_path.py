#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

# 项目目录
object_dir = os.path.dirname(os.path.dirname(__file__))

# 公共方法目录
common_dir = os.path.join(object_dir, "common")

# 配置文件目录
configs_dir = os.path.join(object_dir, "configs")

# 输出文件目录
outputs_dir = os.path.join(object_dir, "outputs")

# 测试数据目录
sources_dir = os.path.join(object_dir, "sources")

# 测试用例目录
cases_dir = os.path.join(object_dir, "testcases")

if __name__ == '__main__':
    print(object_dir)
    print(common_dir)
    print(configs_dir)
    print(outputs_dir)
    print(sources_dir)
    print(cases_dir)
