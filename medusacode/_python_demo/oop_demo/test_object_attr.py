#!/usr/bin/env python
# coding:utf-8

"""
hasattr(object, name)
    The arguments are an object and a string.
    The result is True if the string is the name of one of the object’s attributes, False if not.
    (This is implemented by calling getattr(object, name) and seeing whether it raises an exception or not.)

getattr(object, name[, default])
    name must be a string.
    Return the value of the named attribute of object.
    If the string is the name of one of the object’s attributes, the result is the value of that attribute.
    For example, getattr(x, 'foobar') is equivalent to x.foobar.
    If the named attribute does not exist, default is returned if provided, otherwise [AttributeError] is raised.

setattr(object, name, value)
    This is the counterpart of getattr().
    The arguments are an object, a string and an arbitrary value.
    The string may name an existing attribute or a new attribute.
    The function assigns the value to the attribute, provided the object allows it.
    For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
"""
"""

getattr(x, 'foobar')  等于  x.foobar

setattr(x, 'foobar', 123)  等于  x.foobar = 123.
"""
print '-------------------------------------------------------------------------------------------------------'
print '-------------------------------------------------------------------------------------------------------'
