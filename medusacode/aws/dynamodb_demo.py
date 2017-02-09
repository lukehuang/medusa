#!/usr/bin/env python
# coding:utf-8

"""
AWS DynamoDB
"""

"""
vagrant@precise64:~/.aws$ pwd
/home/vagrant/.aws
vagrant@precise64:~/.aws$ cat config
[default]
region = cn-center-1
vagrant@precise64:~/.aws$ cat credentials
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
"""

aws_access_key_id = 'AKIAIOSFODNN7EXAMPLE'
aws_secret_access_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

from boto.dynamodb2.layer1 import DynamoDBConnection

# Connect to DynamoDB Local
conn = DynamoDBConnection(
    host='192.168.33.10',
    port=8888,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    is_secure=False)
print conn
# DynamoDBConnection:192.168.33.10

# List all local tables
tables = conn.list_tables()
print tables
# {u'TableNames': []}
