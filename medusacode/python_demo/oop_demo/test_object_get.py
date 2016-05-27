#!/usr/bin/env python
# coding:utf-8

"""
__getattribute__, __getattr__, __get__ 都是访问属性的方法

object.__getattribute__(self, name)
    通过实例访问属性时无条件被调用。
    如果类中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常）。
    此方法应该返回一个属性值或抛出AttributeError异常。

object.__getattr__(self, name)
    当一般位置找不到属性的时候(该属性既不是实例属性，也不是类属性)，会调用__getattr__()，
    此方法应该返回一个属性值或抛出AttributeError异常。

object.__get__(self, instance, owner)
    如果类定义了__get__()，则这个类就可以称为descriptor。
    调用此方法获取类属性或实例属性；
    owner是所有者的类，
    instance是访问descriptor的实例（通过类访问的话，instance则为None），
    此方法应该返回一个属性值或抛出AttributeError异常。
    （descriptor的实例自己访问自己不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义）
"""
"""
每次通过实例访问属性，都会经过__getattribute__函数。
当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。
每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。

注意:
    当使用类访问不存在的变量时，不会经过__getattr__函数。
    而descriptor不存在此问题，只是把instance标识为none而已。
"""
print '-------------------------------------------------------------------------------------------------------'
class A(object):
    va = 'ABCDE'

    def __getattribute__(self, item):
        print '(A.__getattribute__)'
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print '(A.__getattr__) : [%s from A.__getattr__]' % item
        return '%s from A.__getattr__' % item

    def __get__(self, instance, owner):
        print '(A.__get__)(instance = %s)(owner = %s) : [%s]' % (instance, owner, self)
        return self

    def __call__(self, *args, **kwargs):
        print '(A.__call__)'


class B(object):
    vb = A()
    pass
print '-------------------------------------------------------------------------------------------------------'
print A.va
# ABCDE

# print A.xxx
# AttributeError: type object 'A' has no attribute 'xxx'

print B.vb
# (A.__get__)(instance = None)(owner = <class '__main__.B'>) : [<__main__.A object at 0x10a8daa10>]
# <__main__.A object at 0x10a8daa10>

print B.vb.va
# (A.__get__)(instance = None)(owner = <class '__main__.B'>) : [<__main__.A object at 0x10a8daa10>]
# (A.__getattribute__)
# ABCDE

print B.vb.xxx
# (A.__get__)(instance = None)(owner = <class '__main__.B'>) : [<__main__.A object at 0x10a8daa10>]
# (A.__getattribute__)
# (A.__getattr__) : [xxx from A.__getattr__]
# xxx from A.__getattr__
print '-------------------------------------------------------------------------------------------------------'
a = A()

print a.va
# (A.__getattribute__)
# ABCDE

print a.xxx
# (A.__getattribute__)
# (A.__getattr__) : [xxx from A.__getattr__]
# xxx from A.__getattr__

b = B()

print b.vb
# (A.__get__)(instance = <__main__.B object at 0x108ebdbd0>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x108ebda10>]
# <__main__.A object at 0x108ebda10>

print b.vb.va
# (A.__get__)(instance = <__main__.B object at 0x108ebdbd0>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x108ebda10>]
# (A.__getattribute__)
# ABCDE
print '-------------------------------------------------------------------------------------------------------'
a()
# (A.__call__)
print '-------------------------------------------------------------------------------------------------------'
