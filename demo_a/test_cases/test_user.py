#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

from demo_a.api.user import User


class TestUser:
    @classmethod
    def setup_class(cls):
        cls.user = User()

    @pytest.mark.parametrize("user_id, name, mobile", [
        ("aaaaaaaaaa", "aaaaaaaaaa", "13537756495"),
        ("aaaaaaaaab", "aaaaaaaaab", "13537756496"),
        ("aaaaaaaaac", "aaaaaaaaac", "13537756497")
    ])
    def test_create(self, user_id, name, mobile):
        print(self.user.create(user_id=user_id, name=name, mobile=mobile))

    @pytest.mark.parametrize("user_id", (
        "aaaaaaaaaa", "aaaaaaaaab", "aaaaaaaaac"
    ))
    def test_delete(self, user_id):
        print(self.user.delete(user_id=user_id))

    @pytest.mark.parametrize("user_id, name, mobile", [
        ("aaaaaaaaaa", "aaaaaaaaaaq", "13537756495"),
        ("aaaaaaaaab", "aaaaaaaaabw", "13537756496"),
        ("aaaaaaaaac", "aaaaaaaaace", "13537756497")
    ])
    def test_update(self, user_id, name, mobile):
        print(self.user.update(user_id=user_id, name=name, mobile=mobile))

    @pytest.mark.parametrize("user_id", (
            "aaaaaaaaaaq", "aaaaaaaaabw", "aaaaaaaaace"
    ))
    def test_get(self, user_id):
        print(self.user.get(user_id=user_id))
