#!/usr/bin/env python
# coding=utf-8


import time
import datetime

def _(dt):
    print type(dt), dt

"""
class time.struct_time
    The type of the time value sequence returned by gmtime(), localtime(), and strptime().
    It is an object with a named tuple interface: values can be accessed by index and by attribute name.
    The following values are present:

    Index 	Attribute 	Values
    0       tm_year     (for example, 1993)
    1       tm_mon      range [1, 12]
    2       tm_mday     range [1, 31]
    3       tm_hour     range [0, 23]
    4       tm_min      range [0, 59]
    5       tm_sec      range [0, 61]; see (2) in strftime() description
    6       tm_wday     range [0, 6], Monday is 0
    7       tm_yday     range [1, 366]
    8       tm_isdst    0, 1 or -1

class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
    The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass.
    The remaining arguments may be ints or longs, in the following ranges:
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= number of days in the given month and year
    0 <= hour < 24
    0 <= minute < 60
    0 <= second < 60
    0 <= microsecond < 1000000
"""

print '----------------------------------------------------------------------------------------------------'
"""
各种时间格式的相互转换
"""
"""
注意区分:
In : datetime.datetime.strftime
Out: <method 'strftime' of 'datetime.date' objects>
In : time.strftime
Out: <function time.strftime>
"""
dt_datetime = datetime.datetime.now()
# <type 'datetime.datetime'>
# 2016-05-18 14:28:05.365674

dt_struct_time = time.localtime()
# <type 'time.struct_time'>
# time.struct_time(tm_year=2016, tm_mon=5, tm_mday=18, tm_hour=14, tm_min=28, tm_sec=5, tm_wday=2, tm_yday=139, tm_isdst=0)

dt_float = time.time()
# <type 'float'>
# 1463553959.7

dt_str = '2016-05-01 10:20:30'
fmt = '%Y-%m-%d %H:%M:%S'
# <type 'str'>
# 2016-05-01 10:20:30

print '----------------------------------------------------------------------------------------------------'
"""
dt_datetime
"""
_(dt_datetime.strftime(fmt))
# <type 'str'> 2016-05-18 15:58:15
_(dt_datetime.timetuple())
# <type 'time.struct_time'> time.struct_time(tm_year=2016, tm_mon=5, tm_mday=18, tm_hour=15, tm_min=58, tm_sec=15, tm_wday=2, tm_yday=139, tm_isdst=-1)
# _(time.mktime(dt_datetime.timetuple()))
# <type 'float'> 1463558295.0
print '----------------------------------------------------------------------------------------------------'
"""
dt_struct_time
"""
_(time.mktime(dt_struct_time))
# <type 'float'> 1463558295.0
# _(datetime.datetime.fromtimestamp(time.mktime(dt_struct_time)))
# <type 'datetime.datetime'> 2016-05-18 15:58:15
_(time.strftime(fmt, dt_struct_time))
# <type 'str'> 2016-05-18 15:58:15
print '----------------------------------------------------------------------------------------------------'
"""
dt_float
"""
_(datetime.datetime.fromtimestamp(dt_float))
# <type 'datetime.datetime'> 2016-05-18 15:58:15.696643
_(time.localtime(dt_float))
# <type 'time.struct_time'> time.struct_time(tm_year=2016, tm_mon=5, tm_mday=18, tm_hour=15, tm_min=58, tm_sec=15, tm_wday=2, tm_yday=139, tm_isdst=0)
# _(datetime.datetime.fromtimestamp(dt_float).strftime(fmt))
# <type 'str'> 2016-05-18 15:58:15
print '----------------------------------------------------------------------------------------------------'
"""
dt_str
"""
_(datetime.datetime.strptime(dt_str, fmt))
# <type 'datetime.datetime'> 2016-05-01 10:20:30
_(time.strptime(dt_str, fmt))
# <type 'time.struct_time'> time.struct_time(tm_year=2016, tm_mon=5, tm_mday=1, tm_hour=10, tm_min=20, tm_sec=30, tm_wday=6, tm_yday=122, tm_isdst=-1)
# _(time.mktime(time.strptime(dt_str, fmt)))
# <type 'float'> 1462069230.0
print '----------------------------------------------------------------------------------------------------'
