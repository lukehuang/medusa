#!/usr/bin/env python
# coding:utf-8

"""
嵌套函数
"""

print '--------------------------------------------------------------------------------------------------'
"""
在嵌套函数中，
每次调用外部函数时，都会执行一次内部函数定义，创建一个新的嵌套函数实例，而其函数体则不会被执行。
"""
"""
嵌套函数可以访问创建它的环境。
一个结果是，外部函数中定义的变量可以在内部函数中引用，即使外部函数已经执行结束。
"""
def outer():
    outer_var = "outer variable"
    def inner():
        return outer_var
    return inner

print outer
# <function outer at 0x107066de8>
print outer()
# <function inner at 0x107066ed8>
print outer()()
# "outer variable"

print '--------------------------------------------------------------------------------------------------'
"""
嵌套函数对象的 __closure__ 属性
"""
"""
当内部嵌套的函数引用外部函数中的变量时，我们说 "嵌套函数相对于引用变量是封闭的" 。
我们可以使用嵌套函数对象的一个特殊属性 __closure__ 来访问这个封闭的变量
"""
func = outer()
print func
# <function inner at 0x1024d70c8>
closure = func.__closure__
print closure
# (<cell at 0x104c3f830: str object at 0x104c3fb90>,)
print closure[0].cell_contents
# "outer variable"
print '--------------------------------------------------------------------------------------------------'
