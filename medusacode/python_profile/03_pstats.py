#!/usr/bin/env python
# coding:utf-8


import cProfile
import profile
import pstats
import sys

from math import hypot
from random import random


def test(tries):
    return sum(hypot(random(), random()) < 1 for _ in range(tries))

"""
class profile.Profile(timer=None, timeunit=0.0, subcalls=True, builtins=True)
    This class is normally only used if more precise control over profiling
    is needed than what the cProfile.run() function provides.

class pstats.Stats(*filenames or profile, stream=sys.stdout)
    This class constructor creates an instance of a “statistics object”
    from a filename (or list of filenames) or from a Profile instance.
    Output will be printed to the stream specified by stream.

    sort_stats(*keys)
        This method modifies the Stats object by sorting it according to the supplied criteria.
        The argument is typically a string identifying the basis of a sort (example: 'time' or 'name').
        The following are the keys currently defined:
        Valid Arg 	Meaning
        'calls' 	call count
        'cumulative' 	cumulative time
        'cumtime' 	cumulative time
        'file' 	file name
        'filename' 	file name
        'module' 	file name
        'ncalls' 	call count
        'pcalls' 	primitive call count
        'line' 	line number
        'name' 	function name
        'nfl' 	name/file/line
        'stdname' 	standard name
        'time' 	internal time
        'tottime' 	internal time

    reverse_order()
        This method for the Stats class reverses the ordering of the basic list within the object.
        Note that by default ascending vs descending order is properly selected based on the sort key of choice.

    print_stats(*restrictions)
        This method for the Stats class prints out a report as described in the profile.run() definition.
        The order of the printing is based on the last sort_stats() operation done on the object.
        The arguments provided (if any) can be used to limit the list down to the significant entries.
        Initially, the list is taken to be the complete set of profiled functions.
        Each restriction is either:
            an integer (to select a count of lines),
            or a decimal fraction between 0.0 and 1.0 inclusive (to select a percentage of lines),
            or a regular expression (to pattern match the standard name that is printed.
        If several restrictions are provided, then they are applied sequentially.
"""

profiler = cProfile.Profile()
profiler.enable()
test(1000000)  # ... do something ...
profiler.disable()
stats = pstats.Stats(profiler, stream=sys.stdout)
stats.sort_stats('cumtime')
stats.reverse_order()
stats.print_stats()

"""
/usr/bin/python /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py
         4000005 function calls in 0.880 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.027    0.027    0.027    0.027 {range}
  1000000    0.096    0.000    0.096    0.000 {math.hypot}
  2000000    0.150    0.000    0.150    0.000 {method 'random' of '_random.Random' objects}
  1000001    0.494    0.000    0.740    0.000 /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)
        1    0.114    0.114    0.854    0.854 {sum}
        1    0.000    0.000    0.880    0.880 /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:14(test)
"""

stats.print_callers()
"""
   Ordered by: cumulative time

Function                                                                                    was called by...
                                                                                                ncalls  tottime  cumtime
{method 'disable' of '_lsprof.Profiler' objects}                                            <-
{range}                                                                                     <-       1    0.030    0.030  /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:14(test)
{math.hypot}                                                                                <- 1000000    0.099    0.099  /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)
{method 'random' of '_random.Random' objects}                                               <- 2000000    0.149    0.149  /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)
/Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)  <- 1000001    0.505    0.753  {sum}
{sum}                                                                                       <-       1    0.114    0.867  /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:14(test)
/Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:14(test)       <-
"""

stats.print_callees()
"""
   Ordered by: cumulative time

Function                                                                                    called...
                                                                                                ncalls  tottime  cumtime
{method 'disable' of '_lsprof.Profiler' objects}                                            ->
{range}                                                                                     ->
{math.hypot}                                                                                ->
{method 'random' of '_random.Random' objects}                                               ->
/Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)  -> 1000000    0.099    0.099  {math.hypot}
                                                                                               2000000    0.149    0.149  {method 'random' of '_random.Random' objects}
{sum}                                                                                       -> 1000001    0.505    0.753  /Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:15(<genexpr>)
/Users/gaohaoning/VM/workspace/medusa/medusacode/python_profile/03_pstats.py:14(test)       ->       1    0.030    0.030  {range}
                                                                                                     1    0.114    0.867  {sum}
"""
