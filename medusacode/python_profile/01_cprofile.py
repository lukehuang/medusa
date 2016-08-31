#!/usr/bin/env python
# coding:utf-8

"""
ncalls
    for the number of calls,
tottime
    for the total time spent in the given function (and excluding time made in calls to sub-functions)
percall
    is the quotient of tottime divided by ncalls
cumtime
    is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.
percall
    is the quotient of cumtime divided by primitive calls
filename:lineno(function)
    provides the respective data of each function
"""

import cProfile
import profile

from math import hypot
from random import random


def test(tries):
    return sum(hypot(random(), random()) < 1 for _ in range(tries))

cProfile.run('test(1000000)')

"""
/usr/bin/python /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/01_cProfile.py
         4000006 function calls in 0.888 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.888    0.888 01_cProfile.py:26(test)
  1000001    0.500    0.000    0.745    0.000 01_cProfile.py:27(<genexpr>)
        1    0.000    0.000    0.888    0.888 <string>:1(<module>)
  1000000    0.097    0.000    0.097    0.000 {math.hypot}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  2000000    0.147    0.000    0.147    0.000 {method 'random' of '_random.Random' objects}
        1    0.031    0.031    0.031    0.031 {range}
        1    0.112    0.112    0.857    0.857 {sum}
"""
