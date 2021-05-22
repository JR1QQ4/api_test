#!/usr/bin/env python
import os.path
from copy import copy
from logging import Formatter
import logging
import pprint

MAPPING = {
    'DEBUG': 37,  # white
    'INFO': 36,  # cyan
    'WARNING': 33,  # yellow
    'ERROR': 31,  # red
    'CRITICAL': 41,  # white on red bg
}

PREFIX = '\033['
SUFFIX = '\033[0m'


class ColoredFormatter(Formatter):

    def __init__(self, pattern):
        Formatter.__init__(self, pattern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        seq = MAPPING.get(levelname, 37)  # default white
        colored_levelname = '{0}{1}m{2}{3}'.format(PREFIX, seq, levelname, SUFFIX)
        colored_record.levelname = colored_levelname
        return Formatter.format(self, colored_record)


class ColoredConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        # Need to make a actual copy of the record
        # to prevent altering the message for other loggers
        # myrecord = copy(record)
        # levelno = myrecord.levelname
        # if levelno >= 50:  # CRITICAL / FATAL
        #     color = '\x1b[41m'  # red
        # elif levelno >= 40:  # ERROR
        #     color = '\x1b[31m'  # red
        # elif levelno >= 30:  # WARNING
        #     color = '\x1b[33m'  # yellow
        # elif levelno >= 20:  # INFO
        #     color = '\x1b[32m'  # green
        # elif levelno >= 10:  # DEBUG
        #     color = '\x1b[35m'  # pink
        # else:  # NOTSET and anything else
        #     color = '\x1b[0m'  # normal
        # myrecord.msg = color + str(myrecord.msg) + '\x1b[0m'  # normal
        # logging.StreamHandler.emit(self, myrecord)

        my_record = copy(record)
        levelname = my_record.levelname
        seq = MAPPING.get(levelname, 37)  # default white
        my_record.msg = '{0}{1}m{2}{3}'.format(PREFIX, seq, str(my_record.msg), SUFFIX)
        logging.StreamHandler.emit(self, my_record)


class HandleLog:
    def __init__(self, name='my_logger', file=None):
        self._log = logging.getLogger(name)

        # Add console handler using our custom ColoredFormatter
        # 重写标准输出流中的处理器 ch = logging.StreamHandler()
        ch = ColoredConsoleHandler()
        ch.setLevel(logging.DEBUG)
        # ch_fmt = "[%(name)s][%(levelname)s]  %(message)s (%(filename)s:%(lineno)d)"
        ch_fmt = "\033[0;32m%(name)s\033[0m \033[0;37m|\033[0m %(levelname)s  " \
                 "\033[0;37m|\033[0m \033[0;35m%(filename)s\033[0m" \
                 "\033[0;37m:\033[0m" \
                 "\033[0;35m%(funcName)s\033[0m" \
                 "\033[0;37m:\033[0m" \
                 "\033[0;35m%(lineno)d\033[0m " \
                 "\033[0;37m-\033[0m %(message)s"
        cf = ColoredFormatter(ch_fmt)
        ch.setFormatter(cf)
        self._log.addHandler(ch)

        if file:
            # Add file handler
            fh = logging.FileHandler(file)
            fh.setLevel(logging.DEBUG)
            # fh_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            fh_fmt = '%(asctime)s | %(name)s | %(levelname)s  | %(filename)s:%(funcName)s:%(lineno)d - %(message)s'
            ff = logging.Formatter(fh_fmt)
            fh.setFormatter(ff)
            self._log.addHandler(fh)

        # Set log level
        self._log.setLevel(logging.DEBUG)

    def get_log(self):
        return self._log

    def debug(self, msg):
        self._log.debug(msg)

    def info(self, msg):
        self._log.info(msg)

    def warning(self, msg):
        self._log.warning(msg)

    def error(self, msg):
        self._log.error(msg)

    def critical(self, msg):
        self._log.critical(msg)


def __get_log(name='my_logger', file=None):
    log = logging.getLogger(name)

    ch = ColoredConsoleHandler()
    ch.setLevel(logging.DEBUG)
    # ch_fmt = "[%(name)s][%(levelname)s]  %(message)s (%(filename)s:%(lineno)d)"
    ch_fmt = "\033[0;32m%(name)s\033[0m \033[0;37m|\033[0m %(levelname)s  " \
             "\033[0;37m|\033[0m \033[0;35m%(filename)s\033[0m" \
             "\033[0;37m:\033[0m" \
             "\033[0;35m%(funcName)s\033[0m" \
             "\033[0;37m:\033[0m" \
             "\033[0;35m%(lineno)d\033[0m " \
             "\033[0;37m-\033[0m %(message)s"
    cf = ColoredFormatter(ch_fmt)
    ch.setFormatter(cf)
    log.addHandler(ch)

    if file:
        # Add file handler
        fh = logging.FileHandler(file)
        fh.setLevel(logging.DEBUG)
        # fh_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        fh_fmt = '%(asctime)s | %(name)s | %(levelname)s  | %(filename)s:%(funcName)s:%(lineno)d - %(message)s'
        ff = logging.Formatter(fh_fmt)
        fh.setFormatter(ff)
        log.addHandler(fh)

    # Set log level
    log.setLevel(logging.DEBUG)

    return log


__log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "logs", "all.log")
logger = HandleLog("my_logger", __log_file)

if __name__ == '__main__':
    # print("显示方式：")
    # print("\033[0;37;40m\tHello World\033[0m")
    #
    # print("前景色：")
    # print("\033[0;30m\tHello World\033[0m")
    # print("\033[0;31m\tHello World\033[0m")
    # print("\033[0;32m\tHello World\033[0m")
    # print("\033[0;33m\tHello World\033[0m")
    # print("\033[0;34m\tHello World\033[0m")
    # print("\033[0;35m\tHello World\033[0m")
    # print("\033[0;36m\tHello World\033[0m")
    # print("\033[0;37m\tHello World\033[0m")
    #
    # print("背景色：")
    # print("\033[0;40m\tHello World\033[0m")
    # print("\033[0;41m\tHello World\033[0m")
    # print("\033[0;42m\tHello World\033[0m")
    # print("\033[0;43m\tHello World\033[0m")
    # print("\033[0;44m\tHello World\033[0m")
    # print("\033[0;45m\tHello World\033[0m")
    # print("\033[0;46m\tHello World\033[0m")
    # print("\033[0;47m\tHello World\033[0m")

    log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "logs", "all.log")

    # Log some stuff
    log1 = __get_log("logger1", log_file)
    log1.debug("app has started")
    log1.info("Logging to 'app.log' in the script dir")
    log1.warning("This is my last warning, take heed")
    log1.error("This is an error")
    log1.critical("He's dead, Jim")

    log2 = HandleLog("logger2", log_file)
    log2.debug("app has started")
    log2.info("Logging to 'app.log' in the script dir")
    log2.warning("This is my last warning, take heed")
    log2.error("This is an error")
    log2.critical("He's dead, Jim")
