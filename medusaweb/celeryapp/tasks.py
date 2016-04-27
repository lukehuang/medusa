# coding: utf-8

"""
use Celery in Django project
"""

import datetime
import time
import random

from celery import task

@task()
def func(n=0):
    start = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    time.sleep(n)
    stop = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    return '[%s] (%s) [%s]' % (start, n, stop)
