#!/usr/bin/env python
# coding:utf-8


from multiprocessing.managers import BaseManager, SyncManager
from multiprocessing import Manager


# class Cache(object):
#     def __init__(self):
#         # self.data = {}
#         self.data = Manager().dict()
#
#     def get(self, key):
#         print '[Cache][get]', key
#         return self.data.get(key)
#
#     def set(self, key, value):
#         print '[Cache][set]', key, value
#         self.data.update({key: value})
#         print '[Cache] = ', self.data

# cache_dict = {}
# cache_dict = Cache()
cache_dict = Manager().dict()

SyncManager.register('get_cache', callable=lambda: cache_dict)
manager = SyncManager(
    address=('0.0.0.0', 8888),
    authkey='course_cache'
)

server = manager.get_server()
server.serve_forever()

print type(manager)
print manager
print type(server)
print server
