#!/usr/bin/env python
# coding:utf-8

"""
数据库报表
"""

from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker


MYSQL_HOST = '10.0.0.123'
MYSQL_PORT = 3306
MYSQL_USER = 'edxapp001'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'edxapp'


engine = create_engine(
    'mysql://%s:%s@%s:%s/%s' % (
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DATABASE)
)
print engine

inspector = inspect(engine)
tables = inspector.get_table_names()
print tables

# Session = sessionmaker(bind=engine)
# print type(Session)
# # <class 'sqlalchemy.orm.session.sessionmaker'>
# print Session
# session = Session()
# print session

