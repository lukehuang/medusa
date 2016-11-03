#!/usr/bin/env python
# coding:utf-8


import datetime
import random

from pymongo import MongoClient
from pymongo import MongoReplicaSetClient

from bson.objectid import ObjectId


mongo_client = MongoClient(
    host='192.168.100.100',
    port=27017,
)

print mongo_client
# MongoClient(host=['192.168.100.100:27017'], document_class=dict, tz_aware=False, connect=True)

# import inspect
# print inspect.getmembers(mongo_client)


database = mongo_client.test_db
print database
# Database(MongoClient(host=['192.168.100.100:27017'], document_class=dict, tz_aware=False, connect=True), u'test_db')


collection = database.test_collection
print collection
# Collection(Database(MongoClient(host=['192.168.100.100:27017'], document_class=dict, tz_aware=False, connect=True), u'test_db'), u'test_collection')


document = {
    'name': ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)) + (''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))).lower(),
    'sex': 'male',
    'tech': 'assassination',
    'weapon': 'sniper rifle',
    'dt': datetime.datetime.now(),
}
doc_id = collection.insert(document)
print doc_id
# 581b1691c567aa1761a33962


document_1 = collection.find_one({'name': 'Sam Fisher'})
print document_1
# {
#   u'name': u'Sam Fisher',
#   u'weapon': u'sniper rifle',
#   u'sex': u'male',
#   u'tech': u'assassination',
#   u'dt': datetime.datetime(2016, 11, 3, 18, 40, 22, 988000),
#   u'_id': ObjectId('581b1416c567aa16f92e4e73')
# }


document_s = collection.find({'name': 'Sam Fisher'})
print document_s
# <pymongo.cursor.Cursor object at 0x102e0fd50>
print document_s.count()
# 3
for doc in document_s:
    print doc
# {u'name': u'Sam Fisher', u'weapon': u'sniper rifle', u'sex': u'male', u'tech': u'assassination', u'dt': datetime.datetime(2016, 11, 3, 18, 40, 22, 988000), u'_id': ObjectId('581b1416c567aa16f92e4e73')}
# {u'name': u'Sam Fisher', u'weapon': u'sniper rifle', u'sex': u'male', u'tech': u'assassination', u'dt': datetime.datetime(2016, 11, 3, 18, 41, 48, 929000), u'_id': ObjectId('581b146cc567aa1701deb44d')}
# {u'name': u'Sam Fisher', u'weapon': u'sniper rifle', u'sex': u'male', u'tech': u'assassination', u'dt': datetime.datetime(2016, 11, 3, 18, 42, 16, 725000), u'_id': ObjectId('581b1488c567aa1708717d70')}


document_2 = collection.find_one({'_id': ObjectId(doc_id)})
print document_2
# {
#   u'name': u'Krbtz',
#   u'weapon': u'sniper rifle',
#   u'sex': u'male',
#   u'tech': u'assassination',
#   u'dt': datetime.datetime(2016, 11, 3, 18, 50, 56, 996000),\
#   u'_id': ObjectId('581b1691c567aa1761a33962')
# }


print database.collection_names()
# [u'test_collection', u'system.indexes']
