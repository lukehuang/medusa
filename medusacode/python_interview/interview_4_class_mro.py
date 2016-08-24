#!/usr/bin/env python
# coding:utf-8

print '----------------------------------------------------------------------------------------------------'
"""
new-style class: breadth-first
新式类的MRO: 广度优先
"""
class A(object):
    attr = 'A'

class B(A):
    # attr = 'B'
    pass

class C(A):
    attr = 'C'

class D(B, C):
    # attr = 'D'
    pass

print D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)

print D.attr
# C
print '----------------------------------------------------------------------------------------------------'
"""
classic class: depth-first
经典类的MRO: 深度优先
"""
class A:
    attr = 'A'

class B(A):
    # attr = 'B'
    pass

class C(A):
    attr = 'C'

class D(B, C):
    # attr = 'D'
    pass

print D.attr
# A
print '----------------------------------------------------------------------------------------------------'
