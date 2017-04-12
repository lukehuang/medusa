#!/usr/bin/env python
# coding=utf-8


import time
import datetime

format = '%Y-%m-%d %H:%M:%S'
print '----------------------------------------------------------------------------------------------------'
dt = '2017-04-15 00:00:00'
s = time.mktime(time.strptime(dt, format))
print dt
print '=>'
print s
print '----------------------------------------------------------------------------------------------------'
s = 1491840000
dt = time.strftime(format, time.localtime(s))
print s
print '=>'
print dt
print '----------------------------------------------------------------------------------------------------'
