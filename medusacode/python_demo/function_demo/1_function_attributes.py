#!/usr/bin/env python
# coding:utf-8

"""
函数属性
"""

def my_func(x):
    """
    my_func doc
    """
    return x**2

print my_func
# <function my_func at 0x10f4d8668>

import inspect
print inspect.getmembers(my_func)
# [
#  ('__call__', <method-wrapper '__call__' of function object at 0x10f4d8668>),
#  ('__class__', <type 'function'>),
#  ('__closure__', None),
#  ('__code__', <code object my_func at 0x10f58f1b0, file "/Users/gaohaoning/VM/workspace/medusa/medusacode/python_demo/function_demo/test_function.py", line 4>),
#  ('__defaults__', None),
#  ('__delattr__', <method-wrapper '__delattr__' of function object at 0x10f4d8668>),
#  ('__dict__', {}),
#  ('__doc__', '\n    my_func doc\n    '),
#  ('__format__', <built-in method __format__ of function object at 0x10f4d8668>),
#  ('__get__', <method-wrapper '__get__' of function object at 0x10f4d8668>),
#  ('__getattribute__', <method-wrapper '__getattribute__' of function object at 0x10f4d8668>),
#  ('__globals__', {'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/Users/gaohaoning/VM/workspace/medusa/medusacode/python_demo/function_demo/test_function.py', 'inspect': <module 'inspect' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/inspect.pyc'>, '__package__': None, 'my_func': <function my_func at 0x10f4d8668>, '__name__': '__main__', '__doc__': None}),
#  ('__hash__', <method-wrapper '__hash__' of function object at 0x10f4d8668>),
#  ('__init__', <method-wrapper '__init__' of function object at 0x10f4d8668>),
#  ('__module__', '__main__'),
#  ('__name__', 'my_func'),
#  ('__new__', <built-in method __new__ of type object at 0x10f3f7528>),
#  ('__reduce__', <built-in method __reduce__ of function object at 0x10f4d8668>),
#  ('__reduce_ex__', <built-in method __reduce_ex__ of function object at 0x10f4d8668>),
#  ('__repr__', <method-wrapper '__repr__' of function object at 0x10f4d8668>),
#  ('__setattr__', <method-wrapper '__setattr__' of function object at 0x10f4d8668>),
#  ('__sizeof__', <built-in method __sizeof__ of function object at 0x10f4d8668>),
#  ('__str__', <method-wrapper '__str__' of function object at 0x10f4d8668>),
#  ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x10f3f7528>),
#  ('func_closure', None),
#  ('func_code', <code object my_func at 0x10f58f1b0, file "/Users/gaohaoning/VM/workspace/medusa/medusacode/python_demo/function_demo/test_function.py", line 4>),
#  ('func_defaults', None),
#  ('func_dict', {}),
#  ('func_doc', '\n    my_func doc\n    '),
#  ('func_globals', {'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/Users/gaohaoning/VM/workspace/medusa/medusacode/python_demo/function_demo/test_function.py', 'inspect': <module 'inspect' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/inspect.pyc'>, '__package__': None, 'my_func': <function my_func at 0x10f4d8668>, '__name__': '__main__', '__doc__': None}),
#  ('func_name', 'my_func')
# ]
