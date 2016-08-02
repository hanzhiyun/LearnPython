#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from mydict import Dict
__author__ = 'Hanzhiyun'


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
# This is the easiest way to run
# if __name__ == '__main__':
#     unittest.main()

# Another method is through the command line parameters of "-m unittest" directly run the unit test
# for example: "py -3 -m unittest mydict_test.py"
