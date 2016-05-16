#!/usr/bin/env python
# coding=utf-8

"""
Python 做编码转换的时候，会借助于内部的编码，转换过程是这样的:
    原有编码 -> 内部编码(unicode) -> 目的编码
"""

def info(var):
    print var, type(var)

print '----------------------------------------------------------------------------------------------------'
"""
Python 中，
[字符串]类型代表人类通用的语言符号，因此[字符串]类型有encode()方法;
[字节]类型代表计算机通用的对象（二进制数据），因此[字节]类型有decode()方法;
"""

s = 'Python字符串'  # 'Python\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
info(s)
# Python字符串 <type 'str'>

u = s.decode('utf-8')  # u'Python\u5b57\u7b26\u4e32'
info(u)
# Python字符串 <type 'unicode'>

ss = u.encode('utf-8')  # 'Python\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
info(ss)
# Python字符串 <type 'str'>

print '----------------------------------------------------------------------------------------------------'
"""
当对str进行编码时，会先用默认编码将自己解码为unicode，然后再将unicode编码为你指定编码。

这就引出了python2.x中在处理中文时，大多数出现错误的原因:
python的默认编码，defaultencoding 是 ascii :
In [1]: import sys
In [2]: sys.getdefaultencoding()
Out[2]: 'ascii'
"""

s = 'Python字符串'
# u = s.encode('utf-8')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
"""
因为没有指定 defaultencoding, 所以它其实在做这样的事情:
"""
# u = s.decode('ascii').encode('utf-8')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
"""
s.encode("utf-8")
等价于
s.decode(defaultencoding).encode("utf-8")
"""

"""
可以通过设置 defaultencoding 方式解决；
也可通过明确指定 decode 方式解决；
"""
u = s.decode(encoding='utf-8').encode('utf-8')  # 'Python\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
info(u)
# Python字符串 <type 'str'>
print '----------------------------------------------------------------------------------------------------'
"""
定义 unicode 的两种方式
"""

unicode_1 = u"Python字符串"  # u'Python\u5b57\u7b26\u4e32'
unicode_2 = unicode("Python字符串", "utf-8")  # u'Python\u5b57\u7b26\u4e32'

info(unicode_1)
# Python字符串 <type 'unicode'>
info(unicode_2)
# Python字符串 <type 'unicode'>

"""
使用 str 创建 unicode 对象时，如果不说明这个 str 的编码格式，那么程序也会使用 defaultencoding:
u = unicode(str)
等价于
u = unicode(str, defaultencoding)
"""
print '----------------------------------------------------------------------------------------------------'
