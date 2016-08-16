#!/usr/bin/env python
# coding:utf-8

print '----------------------------------------------------------------------------------------------------'
def multipliers():
    return [lambda x: i * x for i in range(4)]

print [m(2) for m in multipliers()]
"""
答案是
[6, 6, 6, 6]
而不是
[0, 2, 4, 6]
"""
"""
上述问题产生的原因是Python闭包的延迟绑定。
这意味着内部函数被调用时，参数的值在闭包内进行查找。
因此，当任何由multipliers()返回的函数被调用时，i的值将在附近的范围进行查找。
那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3。
"""
print '----------------------------------------------------------------------------------------------------'
"""
一种解决方法就是用Python生成器
"""
def multipliers():
    for i in range(4):
        yield lambda x: i * x

print [m(2) for m in multipliers()]
# [0, 2, 4, 6]
print '----------------------------------------------------------------------------------------------------'
"""
另外一个解决方案就是创造一个闭包，利用默认函数立即绑定。
"""
def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

print [m(2) for m in multipliers()]
# [0, 2, 4, 6]
print '----------------------------------------------------------------------------------------------------'
"""
还有种替代的方案是，使用偏函数
"""
from functools import partial
from operator import mul

def multipliers():
    return [partial(mul, i) for i in range(4)]

print [m(2) for m in multipliers()]
# [0, 2, 4, 6]
print '----------------------------------------------------------------------------------------------------'
