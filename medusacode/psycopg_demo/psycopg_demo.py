#!/usr/bin/env python
# coding:utf-8


import psycopg2


class PSQL:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='192.168.100.111',
            port=5432,
            user='medusa',
            password='medusa',
            dbname='medusa'
        )
        self.cursor = self.conn.cursor()
        pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        pass

    def sql(self, cmd):
        self.cursor.execute(str(cmd))
        result = self.cursor.fetchone()
        while result:
            result = self.cursor.fetchone()
        return result

    def sql_all(self, cmd):
        self.cursor.execute(str(cmd))
        result = self.cursor.fetchall()
        return result


print '----------------------------------------------------------------------------------------------------'

psql = PSQL()
rows = psql.sql_all('select * from myapp_news;')

for row in rows:
    print row[0], row[1]
    pass
