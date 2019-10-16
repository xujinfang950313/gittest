#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
import pytest
def test_one():
    assert 'i' in 'hello'
def test_two():
    assert 'o' in 'hello'
class Test_yyy():
   def test_two(self):
       assert 1==1
   def test_ww(self):
       assert 2==9

if __name__=='__main__':
    pytest.main(['-k','two','test_day1.py '])