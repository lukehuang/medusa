#!/usr/bin/env python
# coding:utf-8

"""
Comprehensions
    Comprehensions are a Python language construct for concisely creating data in lists, dictionaries and sets.
    List comprehensions are included in Python 2 while dictionary and set comprehensions were introduced to
    the language in Python 3.
"""

"""
List comprehension
"""
ll = [i*i for i in range(10)]
print ll
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
Set comprehension
"""
ss = {i*i for i in range(10)}
print ss
# set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])

"""
Dictionary comprehension
"""
dd = {i: i*i for i in range(10)}
print dd
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

ddd = {k: v for k, v in dd.items()}
print ddd
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
