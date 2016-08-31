#!/usr/bin/env python
# coding:utf-8

"""
sys.settrace(tracefunc)
    Set the system’s trace function, which allows you to implement a Python source code debugger in Python.
    The function is thread-specific; for a debugger to support multiple threads, it must be registered
    using settrace() for each thread being debugged.

    Trace functions should have three arguments: frame, event, arg.
        frame is the current stack frame.
        event is a string: 'call', 'line', 'return', 'exception', 'c_call', 'c_return', or 'c_exception'.
        arg depends on the event type.

    The trace function is invoked (with event set to 'call') whenever a new local scope is entered;
    it should return a reference to a local trace function to be used that scope,
    or None if the scope shouldn’t be traced.

    The local trace function should return a reference to itself
    (or to another function for further tracing in that scope),
    or None to turn off tracing in that scope.
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

sys.settrace(func)
# sys.setprofile(func)

calculate(1000000)
"""
<frame object at 0x107995050> call None 1.19209289551e-06
<frame object at 0x10798d050> call None
"""
