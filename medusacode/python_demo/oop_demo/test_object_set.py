#!/usr/bin/env python
# coding:utf-8

"""
"""
"""
"""
print '-------------------------------------------------------------------------------------------------------'
class A(object):
    va = 'ABCDE'

    # [1]
    # def __getattribute__(self, item):
    #     print '(A.__getattribute__)'
    #     return object.__getattribute__(self, item)

    # [2]
    def __getattribute__(self, item):
        print '(A.__getattribute__)'
        return super(A, self).__getattribute__(item)

    def __getattr__(self, item):
        print '(A.__getattr__) : [%s from A.__getattr__]' % item
        return '%s from A.__getattr__' % item

    def __get__(self, instance, owner):
        print '(A.__get__)(instance = %s)(owner = %s) : [%s]' % (instance, owner, self)
        return self

    def __call__(self, *args, **kwargs):
        print '(A.__call__)'

    def __setattr__(self, key, value):
        print '(A.__setattr__)(key = %s)(value = %s)' % (key, value)
        return super(A, self).__setattr__(key, value)

    def __set__(self, instance, value):
        print '(A.__set__)(instance = %s)(value = %s)' % (instance, value)


class B(object):
    vb = A()
    pass
print '-------------------------------------------------------------------------------------------------------'
a = A()

a.xxx = 'XXX'
# (A.__setattr__)(key = xxx)(value = XXX)

print a.xxx
# (A.__getattribute__)
# XXX
print '-------------------------------------------------------------------------------------------------------'
b = B()

print b.vb
# (A.__get__)(instance = <__main__.B object at 0x102c5bb50>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x102c5ba10>]
# <__main__.A object at 0x102c5ba10>

b.vb = A()
# (A.__set__)(instance = <__main__.B object at 0x10e001b50>)(value = <__main__.A object at 0x10e001bd0>)
print '-------------------------------------------------------------------------------------------------------'
