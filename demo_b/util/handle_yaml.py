#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml


class HandleYaml:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as f:
            self.y = yaml.safe_load(f)

    def get_values(self):
        return self.y.values()

    def get_keys(self):
        return self.y.keys()

    def get_items(self):
        return self.y.items()

    def get_section(self, name='token'):
        return self.y.get(name)

    def update(self, key, value):
        temp = self.y.copy()

        def find_and_change(data):
            for k, v in data.items():
                if k == key:
                    data[k] = value
                if type(v) is dict:
                    find_and_change(v)
            else:
                return data

        print(find_and_change(temp))
        with open(self.file_path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(temp, f)


if __name__ == '__main__':
    import os
    from demo_b.util.handle_path import conf_dir

    token_yaml = os.path.join(conf_dir, "token.yaml")
    hy = HandleYaml(token_yaml)
    print(hy.get_values())
    print(hy.get_items())
    print(hy.get_section())
    # print(hy.update("method", "post"))
