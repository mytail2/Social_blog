#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app import create_app, db
from flask import current_app

class BasicsTestCase(unittest.TestCase):

    def setUp(self):  #测试函数执行前执行：创建程序实例， 推送上下文， 创建数据库
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):  #测试函数执行完毕后执行， 删除数据库， 退出上下文

        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):  #以test开头的都是测试函数

        self.assertFalse(current_app is None)

    def test_app_is_testing(self):

        self.assertTrue(self.app.config['TESTING'])
