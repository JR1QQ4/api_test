#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import unittest

from unittestreport import TestRunner

from demo_c.common.handle_path import outputs_dir, cases_dir

if __name__ == '__main__':
    # res = re.match(r'(\d+)?(<=|<)?length(<=|<|=)?(\d+)?', '64<length')
    # print(res.groups())
    # print(res.group(1), res.group(4))

    discover = unittest.defaultTestLoader.discover(cases_dir, pattern='test*.py')
    report_dir = os.path.join(outputs_dir, 'reports')
    suite = unittest.TestSuite()
    suite.addTest(discover)
    runner = TestRunner(suite,  # 测试套件（必传）
                        tester='jr1qq4',  # 测试人员名称
                        filename="test_report.html",  # 指定报告文件名
                        report_dir=report_dir,  # 指定存放报告路径
                        title='企业微信成员管理接口测试',  # 指定测试报告的标题
                        desc='使用unittest驱动的接口测试报告',
                        templates=2)  # 可以指定1，2，3三个风格的模板
    runner.run()
