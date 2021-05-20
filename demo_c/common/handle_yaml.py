#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
import os


class HandleYaml:
    def __init__(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            self.y = yaml.safe_load(f)

    def items(self):
        return list(self.y.items())


file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "my.yaml")
handle_yaml = HandleYaml(file_path)
print(handle_yaml.items())
