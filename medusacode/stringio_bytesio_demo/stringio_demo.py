#!/usr/bin/env python
# coding:utf-8

"""
StringIO — Read and write strings as files
    This module implements a file-like class, StringIO, that reads and writes a string buffer (also known as memory files).
    (See the description of file objects for operations (section File Objects)).
    (For standard strings, see str and unicode.)
"""
"""
class StringIO.StringIO([buffer])
    When a StringIO object is created, it can be initialized to an existing string by passing the string to the constructor.
    If no string is given, the StringIO will start empty.
    In both cases, the initial file position starts at zero.

StringIO.getvalue()
    Retrieve the entire contents of the “file” at any time before the StringIO object’s close() method is called.

StringIO.close()
    Free the memory buffer. Attempting to do further operations with a closed StringIO object will raise a ValueError.
"""

from StringIO import StringIO

string_file = StringIO()
print string_file
# <StringIO.StringIO instance at 0x101eaa1b8>

string_file.write('first line \n')
print string_file.getvalue()
# first line

string_file.write('second line \n')
print string_file.getvalue()
# first line
# second line

string_file.close()
