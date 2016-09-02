#!/usr/bin/env python
# coding:utf-8

"""
class io.BytesIO([initial_bytes])
    A stream implementation using an in-memory bytes buffer. It inherits BufferedIOBase.
    The argument initial_bytes is an optional initial bytes.
"""
"""
getvalue()
    Return bytes containing the entire contents of the buffer.

read1()
    In BytesIO, this is the same as read().
"""

from io import BytesIO

bytes_file = BytesIO()
print bytes_file
# <_io.BytesIO object at 0x107270410>

number_bytes = bytes_file.write('中文'.decode(encoding='utf-8').encode(encoding='utf-8'))
print bytes_file.getvalue()
# 中文
print number_bytes
# 6

bytes_file.close()
