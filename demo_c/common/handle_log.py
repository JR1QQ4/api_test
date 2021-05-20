#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging

from handle_conf import conf

# from colorama import Fore
#
# COLORS = {
#     'DEBUG': Fore.BLUE,
#     'INFO': Fore.LIGHTWHITE_EX,
#     'WARNING': Fore.YELLOW,
#     'ERROR': Fore.RED,
#     'CRITICAL': Fore.LIGHTRED_EX
# }
#
#
# class ColoredFormatter(logging.Formatter):
#     def __init__(self, msg, is_colored=True):
#         logging.Formatter.__init__(self, msg)
#         self.is_colored = is_colored
#
#     def format(self, record):
#         if self.is_colored:
#             level_name = record.levelname
#             message = str(record.msg)
#             if level_name in COLORS:
#                 level_name_color = COLORS[level_name] + level_name
#                 message_color = COLORS[level_name] + message
#                 record.levelname = level_name_color
#                 record.msg = message_color
#         return logging.Formatter.format(self, record)
#
#
# def get_log(file_path=None):
#     fmt = Fore.GREEN + "%(asctime)s " + Fore.LIGHTWHITE_EX + "|" + Fore.RESET + " %(levelname)s  " \
#           + Fore.LIGHTWHITE_EX + "|" + Fore.MAGENTA + " %(filename)s" + Fore.LIGHTWHITE_EX + ":" \
#           + Fore.MAGENTA + "%(funcName)s" + Fore.LIGHTWHITE_EX + ":" + Fore.MAGENTA \
#           + "%(lineno)d " + Fore.LIGHTWHITE_EX + "-" + Fore.RESET + " %(message)s"
#     log_level = logging.DEBUG
#     color_fmt = ColoredFormatter(fmt)
#     std_h = logging.StreamHandler()
#     std_h.setLevel(log_level)
#     std_h.setFormatter(color_fmt)
#
#     log1 = logging.getLogger("my_logger")
#     log1.setLevel(log_level)
#     log1.addHandler(std_h)
#
#     if file_path:
#         file_h = logging.FileHandler(file_path)
#         file_h.setLevel(log_level)
#         fmt1 = "%(asctime)s | %(levelname)s  | %(module)s:%(funcName)s:%(lineno)d - %(message)s"
#         color_fmt.is_colored = False
#         file_fmt = logging.Formatter(fmt1)
#         file_h.setFormatter(file_fmt)
#         log1.addHandler(file_h)
#
#     return log1
#
#
# if __name__ == '__main__':
#     logger = get_log("log_test.log")
#     logger.info(123123)
#     logger.debug(123123)
#     logger.error(123123)
#     logger.warning(123123)
import os.path


class MyLogger(logging.Logger):
    def __init__(self, name, level='INFO', file=None):
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


__file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results",
                           conf.get('log', 'file_name'))
logger = MyLogger(conf.get('log', 'name'), level=conf.get('log', 'level'), file=__file_path)

if __name__ == '__main__':
    logger1 = MyLogger("my_logger", file="log_test.log")
    logger1.info("这是我的第一个日志信息！This is my first log info.")
    test()
    LogTest.get_log()
