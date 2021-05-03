#!/usr/bin/python
# -*- coding:utf-8 -*-
from openpyxl import load_workbook


class HandleExcel:
    def __init__(self, file_path):
        wb = load_workbook(file_path)


if __name__ == '__main__':
    he = HandleExcel("")
