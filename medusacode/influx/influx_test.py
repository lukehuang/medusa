#!/usr/bin/env python
# coding:utf-8

"""
InfluxDB
"""
"""
InfluxDB vs SQL:
    InfluxDB measurement <====> SQL database table.
    InfluxDB tags <====> indexed columns in an SQL database.
    InfluxDB fields <====> unindexed columns in an SQL database.
    InfluxDB points  <====> SQL rows.
    InfluxDB’s continuous queriesand and retention policies <====> stored procedures in an SQL database.
"""
"""
Line Protocol
Syntax:
    <measurement>[,<tag_key>=<tag_value>[,<tag_key>=<tag_value>]] <field_key>=<field_value>[,<field_key>=<field_value>] [<timestamp>]
"""

import random
import datetime

from influxdb import InfluxDBClient

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
idb_client = InfluxDBClient(
    host='192.168.100.100',
    port=8086,
    username='root',
    password='root',
    # database='demo',
)
print idb_client
# <influxdb.client.InfluxDBClient object at 0x110406410>

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
# ret = idb_client.drop_database('demo')
ret = idb_client.create_database('demo')
print ret
# None

json_body = [
    {
        "measurement":
            "measurement_01",
        "tags": {
            "tag_01": ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)),
            "tag_02": ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)),
        },
        "fields": {
            "field_01": random.random(),
            "field_02": random.random(),
        },
        "time":
            datetime.datetime.now().isoformat("T") + "Z",
    }
]
ret = idb_client.write_points(
    database='demo',
    points=json_body,
)
print ret
# True

ret = idb_client.query(
    database='demo',
    query='select * from measurement_01',
    # query="select * from measurement_name where host = 'host_01' ",
)
print ret
# ResultSet({
#   '(u'measurement_01', None)': [
#     {
#       u'tag_01': u'VMTA',
#       u'field_02': 0.767770356044,
#       u'field_01': 0.614893768776,
#       u'tag_02': u'KVYD',
#       u'time': u'2017-03-07T18:52:11.308093952Z'
#     },
#     {
#       u'tag_01': u'HTIA',
#       u'field_02': 0.205036766905,
#       u'field_01': 0.825553069947,
#       u'tag_02': u'FYUH',
#       u'time': u'2017-03-07T18:52:31.095618048Z'
#     }
#   ]
# })

"""
ResultSet.keys():
    List of keys. Keys are tuples (serie_name, tags)
"""
print ret.keys()
# [(u'measurement_01', None)]

"""
ResultSet.items():
    List of tuples, (key, generator)
"""
print ret.items()
# [((u'measurement_01', None), <generator object _get_points_for_serie at 0x10be51190>)]

print ret.raw
# {
#   u'series': [
#     {
#       u'values': [
#         [
#           u'2017-03-07T18:52:11.308093952Z',
#           0.614893768776,
#           0.767770356044,
#           u'VMTA',
#           u'KVYD'
#         ],
#         [
#           u'2017-03-07T18:52:31.095618048Z',
#           0.825553069947,
#           0.205036766905,
#           u'HTIA',
#           u'FYUH'
#         ]
#       ],
#       u'name': u'measurement_01',
#       u'columns': [
#         u'time',
#         u'field_01',
#         u'field_02',
#         u'tag_01',
#         u'tag_02'
#       ]
#     }
#   ],
#   u'statement_id': 0
# }
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
