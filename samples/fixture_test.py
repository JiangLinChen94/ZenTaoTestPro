#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/5/10 17:36

import unittest

def setUpModule():
    print(">>>>>>>>>>测试模块开始<<<<<<<<<<")

def tearDownModule():
    print(">>>>>>>>>>测试模块开始<<<<<<<<<<")


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('✈✈✈✈测试类开始执行✈✈✈✈!')

    def setUp(self) -> None:
        print('♥❤♥❤测试方法开始执行♥❤♥❤!')

    def tearDown(self) -> None:
        print('♥❤♥❤测试方法执行完毕♥❤♥❤!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('✈✈✈✈测试类执行完毕✈✈✈✈!')

    def test_case1(self):
        print("test_case1")

    def test_case2(self):
        print("test_case2")

if __name__ == '__main__':
    unittest.main()

