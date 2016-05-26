#!/usr/bin/env python
# coding:utf-8

"""
descriptor
"""
"""
definition:
    In general, a descriptor is an object attribute with "binding behavior",
    one whose attribute access has been overridden by methods in the descriptor protocol.
    Those methods are __get__(), __set__(), and __delete__().
    If any of those methods are defined for an object, it is said to be a descriptor.

定义:
    descriptor 是实现了__get__(), __set__(), __delete__()方法的类的实例(对象)。
    任何实现 __get__，__set__，__delete__ 方法中一至多个的类的对象，都是 descriptor 对象。
"""
"""
Descriptor Protocol
    descr.__get__(self, obj, type=None) --> value
    descr.__set__(self, obj, value) --> None
    descr.__delete__(self, obj) --> None

    That is all there is to it. Define any of these methods and an object is considered a descriptor
    and can override default behavior upon being looked up as an attribute.

    If an object defines both __get__() and __set__(), it is considered a data descriptor.
    Descriptors that only define __get__() are called non-data descriptors
    (they are typically used for methods but other uses are possible).

    Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary.
    If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence.
    If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

    To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an AttributeError when called.
    Defining the __set__() method with an exception raising placeholder is enough to make it a data descriptor.
"""
# -------------------------------------------------------------------------------------------------------
class NonNegative(object):
    def __init__(self):
        self.dict = dict()
        pass

    def __get__(self, instance, owner):
        print '(descriptor get) %s' % self.dict[instance]
        return self.dict[instance]

    def __set__(self, instance, value):
        print '(descriptor set) %s' % value
        if value < 0:
            raise ValueError('value can not be negative')
        self.dict[instance] = value

class Score(object):
    """
    NonNegative 实例
    是完全通过类属性模拟实例属性，
    因此实例属性其实根本不存在。
    """
    score = NonNegative()  # descriptor 对象
    pid = NonNegative()  # descriptor 对象

    def __init__(self, pid, score):
        """
        通过在 __init__() 内直接调用类属性,实现对实例属性初始化赋值的模拟.
        """
        self.pid = pid
        self.score = score

    def check(self):
        if self.score >= 60:
            print 'PASS'
        else:
            print 'FAIL'

# -------------------------------------------------------------------------------------------------------
s1 = Score(1, 90)
# (descriptor set) 1
# (descriptor set) 90

s1.score
# (descriptor get) 90

s1.score = 61
# (descriptor set) 61

s1.check()
# (descriptor get) 61
# PASS

s1.score = 59
# (descriptor set) 59

s1.check()
# (descriptor get) 59
# FAIL
# -------------------------------------------------------------------------------------------------------
