#!/usr/bin/env python
# coding:utf-8

"""
逐行分析内存使用
"""
"""
memory_profiler

vagrant@precise64:~$ pip install memory_profiler
"""

@profile
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

print 'ret = %s' % calculate(10000)

"""
vagrant@precise64:/home/workspace/medusa/medusacode/python_demo/performance_analysis$ python -m memory_profiler 02_memory_profiler_demo.py
ret = 0
Filename: 02_memory_profiler_demo.py

Line #    Mem usage    Increment   Line Contents
================================================
     8   21.047 MiB    0.000 MiB   @profile
     9                             def calculate(n):
    10   21.047 MiB    0.000 MiB       s = 0
    11   21.398 MiB    0.352 MiB       for i in range(n):
    12   21.398 MiB    0.000 MiB           s += i
    13   21.398 MiB    0.000 MiB       for i in xrange(n):
    14   21.398 MiB    0.000 MiB           s += i
    15   21.547 MiB    0.148 MiB       for i in range(n):
    16   21.547 MiB    0.000 MiB           s *= i
    17   21.547 MiB    0.000 MiB       for i in xrange(n):
    18   21.547 MiB    0.000 MiB           s *= i
    19   21.547 MiB    0.000 MiB       return s
"""
