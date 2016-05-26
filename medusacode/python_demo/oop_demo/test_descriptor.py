#!/usr/bin/env python
# coding:utf-8

"""
descriptor

definition:
    In general, a descriptor is an object attribute with “binding behavior”,
    one whose attribute access has been overridden by methods in the descriptor protocol.
    Those methods are __get__(), __set__(), and __delete__().
    If any of those methods are defined for an object, it is said to be a descriptor.

定义:
    descriptor 就是实现了__get__(), __set__(), __delete__()方法的类。
    任何实现 __get__，__set__，__delete__ 方法中一至多个的类，都是 descriptor 对象。

"""

# -------------------------------------------------------------------------------------------------------
class NonNegative(object):
    def __init__(self):
        self.dict = dict()
        pass

    def __get__(self, instance, owner):
        print '(descriptor get)'
        return self.dict[instance]

    def __set__(self, instance, value):
        print '(descriptor set)'
        if value < 0:
            raise ValueError('value can not be negative')
        self.dict[instance] = value

class Score(object):
    score = NonNegative()

    def __init__(self, pid, score):
        self.pid = pid
        if score < 0:
            raise ValueError('value can not be negative')
        self.score = score

    def check(self):
        if self.score >= 60:
            print 'PASS'
        else:
            print 'FAIL'

# -------------------------------------------------------------------------------------------------------
s1 = Score(1, 90)
# (descriptor set)

print s1.score
# (descriptor get)
# 90

s1.score = 61
# (descriptor set)

s1.check()
# (descriptor get)
# PASS

s1.score = 59
# (descriptor set)

s1.check()
# FAIL
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
