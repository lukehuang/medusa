#!/usr/bin/env python
# coding=utf-8

"""
蒙特卡洛算法计算圆周率
"""

from math import hypot
from random import random
import time
import os
import thread

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
    print '[process: %s][thread: %s]' % (os.getpid(), thread.get_ident())
    return sum(hypot(random(), random()) < 1 for _ in range(tries))


@timeit
def calc_pi(tries, n):
    # ------------------------------------------------------------------------------------------
    from eventlet import GreenPool
    pool = GreenPool()
    result = pool.imap(test, [tries]*n)  # eventlet
    # ------------------------------------------------------------------------------------------
    pi = 4.0 * sum(result)/(tries * n)
    return pi

pi = calc_pi(1000000, 10)
print 'pi = %s' % pi
# delta = 3.96094918251
# pi = 3.1408468
