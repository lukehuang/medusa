#!/usr/bin/env python
# coding=utf-8

"""
Python 做编码转换的时候，会借助于内部的编码，转换过程是这样的:
    原有编码 -> 内部编码(unicode) -> 目的编码
"""

import codecs

def info(var):
    print var, type(var), str(var), repr(var)

print '----------------------------------------------------------------------------------------------------'
s = 'Python字符串'  # 'Python\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
info(s)
# Python字符串 <type 'str'>

"""
原有编码 -> 内部编码(unicode)
"""
obj = codecs.decode(s, 'utf-8')
# info(obj)
# <type 'unicode'>

print '----------------------------------------------------------------------------------------------------'
"""
内部编码(unicode) -> 目的编码
"""
for encoding in ['ascii', 'utf-8', 'big5', 'gb2312', 'gbk']:
    try:
        enc = codecs.encode(obj, encoding)
        info(enc)
    except Exception, e:
        print type(e), e
        continue

# <type 'exceptions.UnicodeEncodeError'> 'ascii' codec can't encode characters in position 6-8: ordinal not in range(128)
# Python字符串 <type 'str'> Python字符串 'Python\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
# Python�r�Ŧ� <type 'str'> Python�r�Ŧ� 'Python\xa6r\xb2\xc5\xa6\xea'
# Python�ַ� <type 'str'> Python�ַ� 'Python\xd7\xd6\xb7\xfb\xb4\xae'
# Python�ַ� <type 'str'> Python�ַ� 'Python\xd7\xd6\xb7\xfb\xb4\xae'
print '----------------------------------------------------------------------------------------------------'

