#!/usr/bin/env python
# coding:utf-8

"""
pickle
    Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”, h
    owever, to avoid confusion, the terms used here are “pickling” and “unpickling”.
"""
"""
The pickle module provides the following functions to make the pickling process more convenient:

pickle.dump(obj, file[, protocol])
    Write a pickled representation of obj to the open file object file. This is equivalent to Pickler(file, protocol).dump(obj).
    If the protocol parameter is omitted, protocol 0 is used. If protocol is specified as a negative value or HIGHEST_PROTOCOL, the highest protocol version will be used.
    file must have a write() method that accepts a single string argument. It can thus be a file object opened for writing, a StringIO object, or any other custom object that meets this interface.

pickle.load(file)
    Read a string from the open file object file and interpret it as a pickle data stream, reconstructing and returning the original object hierarchy. This is equivalent to Unpickler(file).load().
    file must have two methods, a read() method that takes an integer argument, and a readline() method that requires no arguments. Both methods should return a string. Thus file can be a file object opened for reading, a StringIO object, or any other custom object that meets this interface.
    This function automatically determines whether the data stream was written in binary mode or not.

pickle.dumps(obj[, protocol])
    Return the pickled representation of the object as a string, instead of writing it to a file.
    If the protocol parameter is omitted, protocol 0 is used. If protocol is specified as a negative value or HIGHEST_PROTOCOL, the highest protocol version will be used.

pickle.loads(string)
    Read a pickled object hierarchy from a string. Characters in the string past the pickled object’s representation are ignored.

"""


import pickle

file = '/Users/gaohaoning/tmp/pickled_file'
obj = set(range(10))
print '-------------------------------------------------------------------------------------------------------'
with open(file, 'wb') as f:
    pickle.dump(obj, f)
    pass

print '-------------------------------------------------------------------------------------------------------'
with open(file, 'rb') as f:
    obj_deserialized = pickle.load(f)
    print obj_deserialized
    print obj == obj_deserialized
    """
    set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    True
    """
    pass

print '-------------------------------------------------------------------------------------------------------'
