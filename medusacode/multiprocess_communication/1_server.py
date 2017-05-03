#!/usr/bin/env python
# coding:utf-8


from multiprocessing.managers import BaseManager

cache_dict = {}

BaseManager.register('get_cache', callable=lambda: cache_dict)
manager = BaseManager(
    address=('0.0.0.0', 8888),
    authkey='course_cache'
)

server = manager.get_server()
server.serve_forever()

print type(manager)
print manager
print type(server)
print server
