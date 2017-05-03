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
dict_proxy = manager.get_cache()

print dict_proxy
# <DictProxy object, typeid 'dict' at 0x103005a10>

dict_proxy.update({
    random.choice('abcdefghijklmnopqrstuvwxyz'): random.randrange(0, 100, 1)
})

print dict_proxy.keys()
