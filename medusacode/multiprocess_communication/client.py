#!/usr/bin/env python
# coding:utf-8


import random
from multiprocessing.managers import BaseManager

BaseManager.register('get_cache')
manager = BaseManager(
    address=('0.0.0.0', 8888),
    authkey='course_cache'
)
manager.connect()
c = manager.get_cache()
print c
c.update({random.choice('abcdefghijklmnopqrstuvwxyz'): random.randrange(0, 100, 1)})
print c
