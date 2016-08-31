#!/usr/bin/env python
# coding:utf-8

"""
profile
    A profile is a set of statistics that describes how often and for how long
    various parts of the program executed.
"""
"""
The Python standard library provides three different implementations of the same profiling interface:
    cProfile
        cProfile is recommended for most users;
        it’s a C extension with reasonable overhead that
        makes it suitable for profiling long-running programs.
        Based on lsprof, contributed by Brett Rosen and Ted Czotter.
    profile
        profile, a pure Python module whose interface is imitated by cProfile,
        but which adds significant overhead to profiled programs.
        If you’re trying to extend the profiler in some way,
        the task might be easier with this module.
        Originally designed and written by Jim Roskind.
    hotshot
        hotshot was an experimental C module that focused on minimizing the overhead of profiling,
        at the expense of longer data post-processing times.
        It is no longer maintained and may be dropped in a future version of Python.

The profile and cProfile modules export the same interface, so they are mostly interchangeable;
    cProfile has a much lower overhead but is newer and might not be available on all systems.
    cProfile is really a compatibility layer on top of the internal _lsprof module.
    The hotshot module is reserved for specialized usage.
"""
