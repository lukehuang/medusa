#!/usr/bin/env python
# coding:utf-8

print '--------------------------------------------------------------------------------------------------'
"""
使用[可变类型](list, dict, set, ...)做函数默认参数时，需要特别小心 !!!
因为[函数定义]只执行一次，所以这些可变类型的数据结构（引用值）只在[函数定义]时创建一次 !!!
即: 相同的可变数据结构将用于所有的函数调用 !!!
"""

def my_func(arg=[]):
    arg.append('*')
    return arg

print my_func()
# ['*']
print my_func()
# ['*', '*']
print my_func()
# ['*', '*', '*']
print '--------------------------------------------------------------------------------------------------'

def my_func(arg1, arg2='2'):
    return 'arg1=%s, args=%s' % (arg1, arg2)

print my_func('1')
# arg1=1, args=2
print my_func(arg1='1')
# arg1=1, args=2

print my_func('1', '9')
# arg1=1, args=9
print my_func('1', arg2='9')
# arg1=1, args=9

"""
传递的所有关键字参数必须匹配一个函数接受的参数
而包含非可选参数的关键字顺序并不重要
"""
print my_func(arg2='9', arg1='1')
# arg1=1, args=9

"""
在函数调用中，关键字参数不得早于非关键字参数
"""
# print my_func(arg2='9')
# TypeError: my_func() takes at least 1 argument (1 given)

# print my_func(arg2='9', '1')
# SyntaxError: non-keyword arg after keyword arg
print '--------------------------------------------------------------------------------------------------'
