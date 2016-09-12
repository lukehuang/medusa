#!/usr/bin/env python
# coding:utf-8

"""
切片(slice)

list[start:stop:step]

如果不指定start和stop具体值,
    当step>0时，start和stop默认值是索引的开头和结尾
    当step<0时，start和stop默认值是索引的结尾和开头

str 的 reverse:
str[::-1]

怎样解释?(理解方法)
step的符号表示一种方向的含义:
    +: 即从左向右看，所以start默认是0，stop默认是索引最大值(n-1)
    -: 即从右向左看，所以start默认是索引最大值(n-1)，stop默认是0
"""

l = range(10)
print l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print l[:]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print l[::]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print l[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print l[0:9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print l[0:-1]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print l[0:-1:-1]  # []
print l[0:-2:-1]  # []

print l[0:9:-1]  # []
print l[9:0:-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
