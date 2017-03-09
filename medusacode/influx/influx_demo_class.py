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
import time
import datetime

from influxdb import InfluxDBClient


HOST = '192.168.100.100'
PORT = 8086
USERNAME = 'root'
PASSWORD = 'root',
DATABASE = 'demo'


class InfluxDBGenerator(object):
    def __init__(self):
        self.idb_client = InfluxDBClient(
            host=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD,
        )

    def create_database(self):
        self.idb_client.create_database(DATABASE)

    def drop_database(self):
        self.idb_client.drop_database(DATABASE)

    def get_info(self):
        ret = self.idb_client.get_list_database()
        print ret
        # [{u'name': u'_internal'}, {u'name': u'demo'}]

    def gen_data(self):
        json_body = [
            {
                "measurement":
                    "measurement_01",
                "tags": {
                    # "tag_01": ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)),
                    # "tag_02": ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)),
                    "tag_01": 'user_01',
                    "tag_02": 'course_01',
                },
                "fields": {
                    "field_01": random.random(),
                    "field_02": random.random(),
                },
                # "time":
                #     datetime.datetime.now().isoformat("T") + "Z",
            }
        ]
        self.idb_client.write_points(
            database=DATABASE,
            points=json_body,
        )
        print 'write_points', datetime.datetime.now()

    def query_data(self):
        ret = self.idb_client.query(
            database=DATABASE,
            query='select * from measurement_01',
            # query="select * from measurement_name where host = 'host_01' ",
        )
        print ret
        print ret.raw
        points_generator = ret.get_points()  # <generator object get_points at 0x10886a2d0>
        for point in points_generator:
            print point

if __name__ == '__main__':
    ig = InfluxDBGenerator()
    # ig.drop_database()
    # ig.create_database()
    ig.get_info()
    ig.gen_data()
    ig.query_data()

    while True:
        ig.gen_data()
        time.sleep(1)
