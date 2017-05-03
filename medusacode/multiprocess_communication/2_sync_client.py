#!/usr/bin/env python
# coding:utf-8


import random
from multiprocessing.managers import BaseManager, SyncManager

BaseManager.register('get_cache')
manager = SyncManager(
    address=('0.0.0.0', 8888),
    authkey='course_cache'
)
manager.connect()
c = manager.get_cache()
print c
c.update({random.choice('abcdefghijklmnopqrstuvwxyz'): random.randrange(0, 100, 1)})
print c
