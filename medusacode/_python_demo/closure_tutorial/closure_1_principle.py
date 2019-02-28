#!/usr/bin/env python
# coding:utf-8

"""
对象: 关联了方法的数据
objects are data with methods attached;
闭包: 关联了数据的方法
closures are functions with data attached;
"""
"""
A closure allows you to bind variables into a function without passing them as parameters.
"""

def make_counter():
    def counter():  # counter() is a closure (also a object)
        counter.i += 1
        return counter.i
    counter.i = 0
    return counter

c1 = make_counter()
c2 = make_counter()

print (c1(), c1(), c2(), c2())
# output:
# (1, 2, 1, 2)
