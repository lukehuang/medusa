#!/usr/bin/env python
# coding:utf-8


from multiprocessing.managers import BaseManager, SyncManager

cache_dict = {}

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
