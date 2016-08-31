#!/usr/bin/env python
# coding:utf-8

"""
逐行计时 & 分析执行频率
"""
"""
line_profiler

vagrant@precise64:~$ pip install line_profiler
vagrant@precise64:~$ which kernprof
/usr/local/bin/kernprof
"""
"""
vagrant@precise64:~$ kernprof --help
Usage: kernprof [-s setupfile] [-o output_file_path] scriptfile [arg] ...

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -l, --line-by-line    Use the line-by-line profiler from the line_profiler
                        module instead of Profile. Implies --builtin.
  -b, --builtin         Put 'profile' in the builtins. Use 'profile.enable()'
                        and 'profile.disable()' in your code to turn it on and
                        off, or '@profile' to decorate a single function, or
                        'with profile:' to profile a single section of code.
  -o OUTFILE, --outfile=OUTFILE
                        Save stats to <outfile>
  -s SETUP, --setup=SETUP
                        Code to execute before the code to profile
  -v, --view            View the results of the profile in addition to saving
                        it.
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
vagrant@precise64:/home/workspace/medusa/medusacode/python_demo/performance_analysis$ kernprof -l -v 01_line_profiler_demo.py
ret = 0
Wrote profile results to 01_line_profiler_demo.py.lprof
Timer unit: 1e-06 s

Total time: 0.107646 s
File: 01_line_profiler_demo.py
Function: calculate at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                           @profile
    30                                           def calculate(n):
    31         1            2      2.0      0.0      s = 0
    32     10001        14565      1.5     13.5      for i in range(n):
    33     10000        14273      1.4     13.3          s += i
    34     10001        12172      1.2     11.3      for i in xrange(n):
    35     10000        12605      1.3     11.7          s += i
    36     10001        12686      1.3     11.8      for i in range(n):
    37     10000        13191      1.3     12.3          s *= i
    38     10001        13724      1.4     12.7      for i in xrange(n):
    39     10000        14426      1.4     13.4          s *= i
    40         1            2      2.0      0.0      return s
"""
