#!/usr/bin/python
# -*- coding:utf-8 -*-
def debug0(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()

    return wrapper


@debug0
def hello0():
    print("hello")


def logging1(level):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print(args)
            print("[{0}]: enter {1}()".format(level, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return outwrapper


@logging1(level="INFO")
def hello1(a, b, c):
    print(a, b, c)


class logging2(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(args)
            print("[{0}]: enter {1}()".format(self.level, func.__name__))
            return func(*args, **kwargs)

        return wrapper


@logging2(level="TEST")
def hello2(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    hello0()
    print("*" * 50)
    hello1("hello,", "good", "morning")
    print("*" * 50)
    hello2("hello,", "good", "morning")
