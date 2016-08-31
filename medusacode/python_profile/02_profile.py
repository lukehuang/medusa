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

profile.run('test(1000000)')

"""
/usr/bin/python /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/02_profile.py
         4000007 function calls in 13.838 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   13.836   13.836 02_profile.py:29(test)
  1000001    6.957    0.000   12.044    0.000 02_profile.py:30(<genexpr>)
  1000000    1.729    0.000    1.729    0.000 :0(hypot)
  2000000    3.358    0.000    3.358    0.000 :0(random)
        1    0.027    0.027    0.027    0.027 :0(range)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    1.764    1.764   13.808   13.808 :0(sum)
        1    0.000    0.000   13.836   13.836 <string>:1(<module>)
        0    0.000             0.000          profile:0(profiler)
        1    0.001    0.001   13.838   13.838 profile:0(test(1000000))
"""
