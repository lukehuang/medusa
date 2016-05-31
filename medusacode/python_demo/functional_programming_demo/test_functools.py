#!/usr/bin/env python
# coding:utf-8

"""
functools — Higher-order functions and operations on callable objects
    The functools module is for higher-order functions: functions that act on or return other functions.
    In general, any callable object can be treated as a function for the purposes of this module.
"""

import functools


print '--------------------------------------------------------------------------------------------------'
"""
functools.reduce(function, iterable[, initializer])
    This is the same function as reduce().
    It is made available in this module to allow writing code more forward-compatible with Python 3.
"""

def func_reduce(x, y):
    return x+y

l = range(6)
ll = functools.reduce(func_reduce, l)
lll = functools.reduce(func_reduce, l, 100)
print l
# [0, 1, 2, 3, 4, 5]
print ll
# 15
print lll
# 115
print '--------------------------------------------------------------------------------------------------'

"""
functools.partial(func[,*args][, **keywords])
    Return a new partial object which when called will behave like
    func called with the positional arguments args and keyword arguments keywords.
    If more arguments are supplied to the call, they are appended to args.
    If additional keyword arguments are supplied, they extend and override keywords.
    Roughly equivalent to:

    def partial(func, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = keywords.copy()
            newkeywords.update(fkeywords)
            return func(*(args + fargs), **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc

    The partial() is used for partial function application which “freezes” some portion of
    a function’s arguments and/or keywords resulting in a new object with a simplified signature.
    For example, partial() can be used to create a callable that behaves like the int() function
    where the base argument defaults to two:

    >>> from functools import partial
    >>> basetwo = partial(int, base=2)
    >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
    >>> basetwo('10010')
    18
"""
"""
partial objects
    partial objects are callable objects created by partial().
    They have three read-only attributes:
        partial.func
            A callable object or function. Calls to the partial object will be forwarded to func with new arguments and keywords.
        partial.args
            The leftmost positional arguments that will be prepended to the positional arguments provided to a partial object call.
        partial.keywords
            The keyword arguments that will be supplied when the partial object is called.

    partial objects are like function objects in that they are callable, weak referencable, and can have attributes.
    There are some important differences.
        For instance, the __name__ and __doc__ attributes are not created automatically.
        Also, partial objects defined in classes behave like static methods
        and do not transform into bound methods during instance attribute look-up.
"""

def my_function(*args, **kwargs):
    print args
    print kwargs
    return args, kwargs

ret = my_function(1, 2, 3, a=11, b=22, c=33)
# (1, 2, 3)
# {'a': 11, 'c': 33, 'b': 22}
print ret
# ((1, 2, 3), {'a': 11, 'c': 33, 'b': 22})

function_partial = functools.partial(my_function, 9, x=99)
ret_partial = function_partial(1, 2, 3, a=11, b=22, c=33)
# (9, 1, 2, 3)
# {'x': 99, 'a': 11, 'c': 33, 'b': 22}
print ret_partial
# ((9, 1, 2, 3), {'x': 99, 'a': 11, 'c': 33, 'b': 22})

print function_partial.func  # <function my_function at 0x1097bf938>
print function_partial.args  # (9,)
print function_partial.keywords  # {'x': 99}
print '--------------------------------------------------------------------------------------------------'

"""
functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
    Update a wrapper function to look like the wrapped function.
    The optional arguments are tuples to specify
    which attributes of the original function are assigned directly to the matching attributes on the wrapper function
    and which attributes of the wrapper function are updated with the corresponding attributes from the original function.
    The default values for these arguments are the module level constants WRAPPER_ASSIGNMENTS
    (which assigns to the wrapper function’s __name__, __module__ and __doc__, the documentation string)
    and WRAPPER_UPDATES (which updates the wrapper function’s __dict__, i.e. the instance dictionary).

    The main intended use for this function is in decorator functions
    which wrap the decorated function and return the wrapper.
    If the wrapper function is not updated, the metadata of the returned function will
    reflect the wrapper definition rather than the original function definition,
    which is typically less than helpful.
"""
"""
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
WRAPPER_UPDATES = ('__dict__',)
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    '''Update a wrapper function to look like the wrapped function

       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    '''
    for attr in assigned:
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper
"""

print functools.WRAPPER_ASSIGNMENTS
# ('__module__', '__name__', '__doc__')

print functools.WRAPPER_UPDATES
# ('__dict__',)

print '************************************************************'
# [1] 装饰器装饰函数后，返回的新函数使用装饰器中 wrapper 的 '__module__', '__name__', '__doc__', __dict__
def my_decorator(f):
    def wrapper(*args, **kwargs):
        """
        doc_string of wrapper
        """
        print '(Calling decorated function)'
        return f(*args, **kwargs)
    return wrapper                                     # !!!!!!!!!!

@my_decorator
def func():
    """
    doc_string of func
    """
    print '(Calling original function)'

func()
# (Calling decorated function)
# (Calling original function)
print func.__module__
# __main__
print func.__name__
# wrapper  # !!!!!!!!!!
print func.__doc__
# doc_string of wrapper  # !!!!!!!!!!
print func.__dict__
# {}
print '************************************************************'
# [2] 装饰器装饰函数后，返回的新函数使用原函数自己的 '__module__', '__name__', '__doc__',
#     原函数的 __dict__ 也会被更新到装饰后的新函数中
def my_decorator(f):
    def wrapper(*args, **kwargs):
        """
        doc_string of wrapper
        """
        print '(Calling decorated function)'
        return f(*args, **kwargs)
    return functools.update_wrapper(wrapper, f)         # !!!!!!!!!!

@my_decorator
def func():
    """
    doc_string of func
    """
    print '(Calling original function)'

func()
# (Calling decorated function)
# (Calling original function)
print func.__module__
# __main__
print func.__name__
# func  # !!!!!!!!!!
print func.__doc__
# doc_string of func  # !!!!!!!!!!
print func.__dict__
# {}
print '************************************************************'
print '--------------------------------------------------------------------------------------------------'




"""
functools.wraps(wrapped[, assigned][, updated])
    This is a convenience function for invoking update_wrapper() as a function decorator when defining a wrapper function.
    It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).
"""
print '--------------------------------------------------------------------------------------------------'
# def my_decorator(f):
#     @functools.wraps(f)
#     def wrapper(*args, **kwargs):
#         print '(Calling decorated function)'
#         return f(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def func():
#     """
#     doc_string of func
#     """
#     print '(Calling original function)'
#
#
# func()
# # (Calling decorated function)
# # (Calling original function)
# print func.__name__
# # func
# print func.__module__
# # __main__
# print func.__doc__
# # doc_string of func
print '--------------------------------------------------------------------------------------------------'
