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


class InfluxDBGenerator(object):
    def __init__(self):
        self.idb_client = InfluxDBClient(
            host='192.168.100.100',
            port=8086,
            username='root',
            password='root',
        )

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
                "time":
                    datetime.datetime.now().isoformat("T") + "Z",
            }
        ]
        self.idb_client.write_points(
            database='demo',
            points=json_body,
        )

    def query_data(self):
        ret = self.idb_client.query(
            database='demo',
            query='select * from measurement_01',
            # query="select * from measurement_name where host = 'host_01' ",
        )
        print ret

if __name__ == '__main__':
    ig = InfluxDBGenerator()
    ig.gen_data()
    ig.query_data()
