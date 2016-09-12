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
    当使用类访问不存在的属性时，不会经过__getattr__函数。
    当使用实例访问不存在的属性时，会经过__getattr__函数。
    而descriptor不存在此问题，只是把instance标识为none而已。
"""
"""
object.__getattribute__(self, name)
    Called unconditionally to implement attribute accesses for instances of the class.
    If the class also defines __getattr__(), the latter will not be called unless
    __getattribute__() either calls it explicitly or raises an AttributeError.
    This method should return the (computed) attribute value or raise an AttributeError exception.
    In order to avoid infinite recursion in this method, its implementation should always call the base class method
    with the same name to access any attributes it needs, for example, object.__getattribute__(self, name).

object.__getattr__(self, name)
    Called when an attribute lookup has not found the attribute in the usual places
    (i.e. it is not an instance attribute nor is it found in the class tree for self).
    name is the attribute name.
    This method should return the (computed) attribute value or raise an AttributeError exception.

object.__getitem__(self, key)
    Called to implement evaluation of self[key].
    For sequence types, the accepted keys should be integers and slice objects.
    Note that the special interpretation of negative indexes (if the class wishes to emulate a sequence type)
    is up to the __getitem__() method.
    If key is of an inappropriate type, TypeError may be raised;
    if of a value outside the set of indexes for the sequence (after any special interpretation of negative values),
    IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError should be raised.

object.__get__(self, instance, owner)
    Called to get the attribute
    of the owner class (class attribute access) or
    of an instance of that class (instance attribute access).
    owner is always the owner class,
    instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner.
    This method should return the (computed) attribute value or raise an AttributeError exception.

getattr(object, name[, default])
    Return the value of the named attribute of object. name must be a string.
    If the string is the name of one of the object’s attributes, the result is the value of that attribute.
    For example, getattr(x, 'foobar') is equivalent to x.foobar.
    If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
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


class B(object):
    vb = A()
    pass
print '-------------------------------------------------------------------------------------------------------'
print A.va
# ABCDE

"""
当使用类访问不存在的属性时，不会经过__getattr__函数。
"""
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

"""
当使用实例访问不存在的属性时，会经过__getattr__函数。
"""
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

print b.vb.xxx
# (A.__get__)(instance = <__main__.B object at 0x1021deb90>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x1021dea10>]
# (A.__getattribute__)
# (A.__getattr__) : [xxx from A.__getattr__]
# xxx from A.__getattr__
print '-------------------------------------------------------------------------------------------------------'
"""
getattr(x, 'foobar')
    is equivalent to
x.foobar
"""
print getattr(A, 'va')
# ABCDE

# print getattr(A, 'xxx')
# AttributeError: type object 'A' has no attribute 'xxx'

print getattr(a, 'va')
# (A.__getattribute__)
# ABCDE

print getattr(a, 'xxx')
# (A.__getattribute__)
# (A.__getattr__) : [xxx from A.__getattr__]
# xxx from A.__getattr__

print getattr(B, 'vb')
# (A.__get__)(instance = None)                              (owner = <class '__main__.B'>) : [<__main__.A object at 0x101673a10>]
# <__main__.A object at 0x101673a10>

print getattr(b, 'vb')
# (A.__get__)(instance = <__main__.B object at 0x10dc3cb90>)(owner = <class '__main__.B'>) : [<__main__.A object at 0x10dc3ca10>]
# <__main__.A object at 0x10dc3ca10>
print '-------------------------------------------------------------------------------------------------------'
a()
# (A.__call__)
print '-------------------------------------------------------------------------------------------------------'
