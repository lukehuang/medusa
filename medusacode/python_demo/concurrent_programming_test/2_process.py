#!/usr/bin/env python
# coding=utf-8

"""
蒙特卡洛算法计算圆周率
"""

from math import hypot
from random import random
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        delta = stop - start
        print 'delta = %s' % delta
        return ret
    return wrapper

def test(tries):
    return sum(hypot(random(), random()) < 1 for _ in range(tries))


@timeit
def calc_pi(tries, n):
    # ------------------------------------------------------------------------------------------
    from multiprocessing import Pool
    pool = Pool(5)
    result = pool.map(test, [tries]*n)  # 进程池
    # ------------------------------------------------------------------------------------------
    pi = 4.0 * sum(result)/(tries * n)
    return pi

pi = calc_pi(1000000, 10)
print 'pi = %s' % pi
# delta = 2.28838086128
# pi = 3.1419656
