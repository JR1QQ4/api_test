#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging


class MyLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO, file=None):
        super(MyLogger, self).__init__(name, level)

        # 日志格式
        fmt = '%(asctime)s | %(levelname)s  | %(module)s:%(funcName)s:%(lineno)d - %(message)s'
        formatter = logging.Formatter(fmt)

        std_h = logging.StreamHandler()
        std_h.setFormatter(formatter)
        self.addHandler(std_h)

        if file:
            file_h = logging.FileHandler(file, encoding='utf-8')
            file_h.setFormatter(formatter)
            self.addHandler(file_h)


def test():
    logger2 = MyLogger("my_logger", file="log_test.log")
    logger2.info("这是我的第二个日志信息！This is my second log info.")


class LogTest:
    @staticmethod
    def get_log():
        logger3 = MyLogger("my_logger", file="log_test.log")
        logger3.info("这是我的第三个日志信息！This is my three log info.")


if __name__ == '__main__':
    logger = MyLogger("my_logger", file="log_test.log")
    logger.info("这是我的第一个日志信息！This is my first log info.")
    test()
    LogTest.get_log()
