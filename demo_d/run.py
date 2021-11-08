#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from unittestreport import TestRunner
from common.handle_path import CASE_DIR, REPORT_DIR


suite = unittest.defaultTestLoader.discover(CASE_DIR)
runner = TestRunner(suite,
                    filename='report.html',
                    report_dir=REPORT_DIR)
runner.run()
