#!/usr/bin/env python
# coding=utf-8

"""
浅拷贝和深拷贝

因为 Python 的赋值语句不是真的复制对象, 只是创建了引用和对象之间的关联。
对于可变集合和包含可变元素的集合，copy 操作有必要，以便可以在改变副本时不改变原始对象。
"""
"""
直接赋值：
    其实就是对象的引用（别名）。

浅拷贝(copy.copy)：
    拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(copy.deepcopy)： 
    完全拷贝了父对象及其子对象。
"""

"""
copy — Shallow and deep copy operations

Assignment statements in Python do not copy objects, they create bindings between a target and an object. 
For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. 
This module provides generic shallow and deep copy operations (explained below).

Interface summary:
    copy.copy(x)
        Return a shallow copy of x.
    
    copy.deepcopy(x)
        Return a deep copy of x.
    
    exception copy.error
        Raised for module specific errors.
"""
"""
The difference between shallow and deep copying is only relevant for compound objects 
(objects that contain other objects, like lists or class instances):

    A shallow copy constructs a new compound object and  then 
    (to the extent possible) inserts references into it to the objects found in the original.
    
    A deep copy constructs a new compound object and then, 
    recursively, inserts copies into it of the objects found in the original.
"""
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
import copy
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""
直接赋值
"""
a = {1: [1, 2, 3]}
b = a
print id(a), id(b)
print id(a[1]), id(b[1])
# 4300366464 4300366464
# 4312587728 4312587728
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""
浅拷贝
"""
a = {1: [1, 2, 3]}
# b = a.copy()
b = copy.copy(a)
print id(a), id(b)
print id(a[1]), id(b[1])
# 4486316952 4486317232
# 4486306992 4486306992
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""
深拷贝
"""
a = {1: [1, 2, 3]}
b = copy.deepcopy(a)
print id(a), id(b)
print id(a[1]), id(b[1])
# 4322304640 4334535856
# 4334525904 4323346768
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
