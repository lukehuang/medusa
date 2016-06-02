#!/usr/bin/env python
# coding:utf-8

"""
closure
"""
"""
闭包可以用来维持状态（与类作用不同）。
在一些简单的情况下，还可以提供一种简洁性与可读性比类更强的解决方案，
"""
print '--------------------------------------------------------------------------------------------------'
"""
使用tech_pro中的一个日志例子来说明这一点。
假设一个非常简单的日志API，它使用基于类的面向对象思想，并可以在不同级别上打印日志：
"""
class Log(object):
    def __init__(self, level):
        self._level = level
    def __call__(self, message):
        print '[%s] %s' % (self._level, message)

log_info = Log('info')
log_info('this is a message')
# [info] this is a message
print '--------------------------------------------------------------------------------------------------'
"""
相同的功能也可以使用闭包来实现。
而且基于闭包的版本更简洁、可读性更好。
"""
def make_log(level):
    def _(message):
        print '[%s] %s' % (level, message)
    return _

log_info = make_log('info')
log_info('this is a message')
# [info] this is a message
print '--------------------------------------------------------------------------------------------------'
