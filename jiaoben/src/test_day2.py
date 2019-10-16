#!/usr/bin/env/ python
# -*- coding:utf-8 -*-

import pytest
# def test_one():
#     assert 'i 'in 'hello'
# def test_two():
#     assert 0==0
#
#
#
#
# if __name__ == '__main__':
#     # pytest.main(['--setup-show','-s','test_day2.py'])
#     pytest.main(['-q', 'test_day2.py'])
#              #--setup--show查看setup开始 和 teardown的结束
#
# import  time
# def jisuan(f):
#     def wrapper():
#         start = time.time()
#         f()
#         end = time.time()
#         print('执行时间为{}'.format(end - start))
#         return  f
#     return wrapper
# def one():
#     print('hello')
#     time.sleep(1)
#     print('word')
# @jisuan
# def two():
#     print('111')
#     time.sleep(2)
#     print('222')
# jisuan(two)()

import pytest
import time
try:
    print('123')
    raise TypeError('hhh')
except :
    print(TypeError)

