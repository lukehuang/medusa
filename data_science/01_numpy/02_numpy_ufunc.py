#!/usr/bin/env python
# coding:utf-8

"""
numpy 提供了两种基本的对象：
    ndarray（N-dimensional array object）: 存储单一数据类型的多维数组
    ufunc（universal function object）: 能够对数组进行处理的函数
"""
"""
ufunc 是一种能对数组的每个元素进行操作的函数。
numpy 内置的许多ufunc函数都是在C语言级别实现的，因此它们的计算速度非常快。
"""

import time
import numpy as np

print '--------------------------------------------------------------------------------'
"""
计时器
"""
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        delta = stop - start
        print 'delta = %s' % delta
        return ret
    return wrapper
print '--------------------------------------------------------------------------------'


@timeit
def work():
    print 'work start'
    time.sleep(1)
    print 'work stop'
    return


work()
