#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
from colorama import Style, Fore

from demo_b.util.handle_path import log_dir


class HandleLog:
    def __init__(self):
        self.file_logger = logging.getLogger("file_logger")
        self.std_logger = logging.getLogger("std_logger")

        # 日志级别 CRITICAL、FATAL、ERROR、WARN、WARNING、INFO、DEBUG、NOTSET
        self.file_logger.setLevel(logging.INFO)
        self.std_logger.setLevel(logging.INFO)

        # 日志输出目录
        all_log_path = os.path.join(log_dir, 'all.log')
        error_log_path = os.path.join(log_dir, 'error.log')

        # 设置日志输出的渠道
        fh_all = logging.FileHandler(all_log_path, encoding='utf-8')
        fh_error = logging.FileHandler(error_log_path, encoding='utf-8')
        fh_all.setLevel(logging.DEBUG)
        fh_error.setLevel(logging.ERROR)
        fh_formatter = logging.Formatter(
            "%(asctime)s, %(name)s, File \"%(filename)s\", line %(lineno)d, 【%(levelname)s】: %(message)s")
        fh_all.setFormatter(fh_formatter)
        fh_error.setFormatter(fh_formatter)

        self.file_logger.addHandler(fh_all)
        self.file_logger.addHandler(fh_error)

        self.sh = logging.StreamHandler()
        self.sh.setLevel(logging.DEBUG)

    def debug(self, msg: str):
        self.file_logger.debug(msg)
        sh_formatter = logging.Formatter(
            Fore.BLUE + "%(asctime)s, File \"%(filename)s\", line %(lineno)d【%(levelname)s】: %(message)s")
        self.sh.setFormatter(sh_formatter)
        self.std_logger.addHandler(self.sh)
        self.std_logger.debug(msg)

    def info(self, msg: str):
        self.file_logger.info(msg)
        sh_formatter = logging.Formatter(
            Fore.GREEN + "%(asctime)s, File \"%(filename)s\", line %(lineno)d【%(levelname)s】: %(message)s")
        self.sh.setFormatter(sh_formatter)
        self.std_logger.addHandler(self.sh)
        self.std_logger.info(msg)

    def warning(self, msg: str):
        self.file_logger.warning(msg)
        sh_formatter = logging.Formatter(
            Fore.YELLOW + "%(asctime)s, File \"%(filename)s\", line %(lineno)d【%(levelname)s】: %(message)s")
        self.sh.setFormatter(sh_formatter)
        self.std_logger.addHandler(self.sh)
        self.std_logger.warning(msg)

    def error(self, msg: str):
        self.file_logger.error(msg)
        sh_formatter = logging.Formatter(
            Fore.RED + "%(asctime)s, File \"%(filename)s\", line %(lineno)d【%(levelname)s】: %(message)s")
        self.sh.setFormatter(sh_formatter)
        self.std_logger.addHandler(self.sh)
        self.std_logger.error(msg)

    def critical(self, msg: str):
        self.file_logger.critical(msg)
        sh_formatter = logging.Formatter(
            Fore.LIGHTRED_EX + "%(asctime)s, File \"%(filename)s\", line %(lineno)d【%(levelname)s】: %(message)s")
        self.sh.setFormatter(sh_formatter)
        self.std_logger.addHandler(self.sh)
        self.std_logger.critical(msg)


if __name__ == '__main__':
    logger = HandleLog()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
