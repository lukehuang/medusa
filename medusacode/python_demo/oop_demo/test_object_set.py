#!/usr/bin/env python
# coding:utf-8

"""
object.__setattr__(self, name, value)
    Called when an attribute assignment is attempted.
    This is called instead of the normal mechanism (i.e. store the value in the instance dictionary).
    name is the attribute name, value is the value to be assigned to it.
        If __setattr__() wants to assign to an instance attribute, it should not simply execute
            self.name = value
            — this would cause a recursive call to itself.
        Instead, it should insert the value in the dictionary of instance attributes, e.g.
            self.__dict__[name] = value.
        For new-style classes, rather than accessing the instance dictionary,
        it should call the base class method with the same name, for example,
            object.__setattr__(self, name, value).

object.__setitem__(self, key, value)
    Called to implement assignment to self[key]. Same note as for __getitem__().
    This should only be implemented
        for mappings if the objects support changes to the values for keys,  or if new keys can be added,
        or for sequences if elements can be replaced.
    The same exceptions should be raised for improper key values as for the __getitem__() method.

object.__set__(self, instance, value)
    Called to set the attribute on an instance(instance) of the owner class to a new value(value).

setattr(object, name, value)
    This is the counterpart of getattr().
    The arguments are an object, a string and an arbitrary value.
    The string may name an existing attribute or a new attribute.
    The function assigns the value to the attribute, provided the object allows it.
    For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
"""
"""
setattr(x, 'foobar', 123)
    is equivalent to
x.foobar = 123
"""
print '-------------------------------------------------------------------------------------------------------'
class A(object):
    va = 'ABCDE'

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
print B.vb
# (A.__get__)(instance = None)                              (owner = <class '__main__.B'>) : [<__main__.A object at 0x1015a3a10>]
# <__main__.A object at 0x1015a3a10>

B.vb = A()
# (nothing here)
print '-------------------------------------------------------------------------------------------------------'
b = B()

print b.vb
# (A.__get__)(instance = <__main__.B object at 0x1015a3a10>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x1015a3b50>]
# <__main__.A object at 0x1015a3b50>

b.vb = A()
# (A.__set__)(instance = <__main__.B object at 0x1015a3a10>)(value = <__main__.A object at 0x1015a3bd0>)
print '-------------------------------------------------------------------------------------------------------'
