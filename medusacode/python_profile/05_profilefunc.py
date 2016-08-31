#!/usr/bin/env python
# coding:utf-8

"""
sys.setprofile(profilefunc)
    Set the system’s profile function, which allows you to implement a Python source code profiler in Python.
    The system’s profile function is called similarly to the system’s trace function (see settrace()),
    but it isn’t called for each executed line of code
    (only on call and return, but the return event is reported even when an exception has been set).
    Also, its return value is not used, so it can simply return None.
"""

import sys
import time

def timer():
    cur_time = time.time()
    while True:
        new_time = time.time()
        delta = new_time - cur_time
        cur_time = new_time
        yield delta

t = timer()
def func(frame, event, arg):
    print frame, event, arg, t.next()


def calculate(n):
    s = 0
    for i in range(n):
        s += i
    for i in xrange(n):
        s += i
    for i in range(n):
        s *= i
    for i in xrange(n):
        s *= i
    return s

# sys.settrace(func)
sys.setprofile(func)

calculate(1000000)
"""
<frame object at 0x1039ba050> call None 5.00679016113e-06
<frame object at 0x1039ba050> c_call <built-in function range> 8.29696655273e-05
<frame object at 0x1039ba050> c_return <built-in function range> 0.0253200531006
<frame object at 0x1039ba050> c_call <built-in function range> 0.0851609706879
<frame object at 0x1039ba050> c_return <built-in function range> 0.0114550590515
<frame object at 0x1039ba050> return 0 0.0932588577271
<frame object at 0x10388bc20> return None 1.50203704834e-05
<frame object at 0x1039b8050> call None
"""
