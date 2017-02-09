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

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
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

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
# Create table
table = conn.create_table(
    table_name='Music',
    key_schema=[
        {
            'AttributeName': "Artist",
            'KeyType': "HASH"
        },
        {
            'AttributeName': "SongTitle",
            'KeyType': "RANGE"
        }
    ],
    attribute_definitions=[
        {
            'AttributeName': "Artist",
            'AttributeType': "S"
        },
        {
            'AttributeName': "SongTitle",
            'AttributeType': "S"
        }
    ],
    provisioned_throughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)
print table
# {
#   u'TableDescription': {
#     u'TableArn': u'arn:aws:dynamodb:ddblocal:000000000000:table/Music',
#     u'AttributeDefinitions': [
#       {
#         u'AttributeName': u'Artist',
#         u'AttributeType': u'S'
#       },
#       {
#         u'AttributeName': u'SongTitle',
#         u'AttributeType': u'S'
#       }
#     ],
#     u'ProvisionedThroughput': {
#       u'NumberOfDecreasesToday': 0,
#       u'WriteCapacityUnits': 1,
#       u'LastIncreaseDateTime': 0.0,
#       u'ReadCapacityUnits': 1,
#       u'LastDecreaseDateTime': 0.0
#     },
#     u'TableSizeBytes': 0,
#     u'TableName': u'Music',
#     u'TableStatus': u'ACTIVE',
#     u'KeySchema': [
#       {
#         u'KeyType': u'HASH',
#         u'AttributeName': u'Artist'
#       },
#       {
#         u'KeyType': u'RANGE',
#         u'AttributeName': u'SongTitle'
#       }
#     ],
#     u'ItemCount': 0,
#     u'CreationDateTime': 1486632161.815
#   }
# }
tt = conn.list_tables()
print tt
# {u'TableNames': [u'Music']}
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
# Describe table
tt = conn.describe_table('Music')
print tt
# {
#   u'Table': {
#     u'TableArn': u'arn:aws:dynamodb:ddblocal:000000000000:table/Music',
#     u'AttributeDefinitions': [
#       {
#         u'AttributeName': u'Artist',
#         u'AttributeType': u'S'
#       },
#       {
#         u'AttributeName': u'SongTitle',
#         u'AttributeType': u'S'
#       }
#     ],
#     u'ProvisionedThroughput': {
#       u'NumberOfDecreasesToday': 0,
#       u'WriteCapacityUnits': 1,
#       u'LastIncreaseDateTime': 0.0,
#       u'ReadCapacityUnits': 1,
#       u'LastDecreaseDateTime': 0.0
#     },
#     u'TableSizeBytes': 0,
#     u'TableName': u'Music',
#     u'TableStatus': u'ACTIVE',
#     u'KeySchema': [
#       {
#         u'KeyType': u'HASH',
#         u'AttributeName': u'Artist'
#       },
#       {
#         u'KeyType': u'RANGE',
#         u'AttributeName': u'SongTitle'
#       }
#     ],
#     u'ItemCount': 0,
#     u'CreationDateTime': 1486632161.815
#   }
# }
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'


print '????????????????????????????????????????????????????????????????????????????????'
# Put item
item = {
    "Artist": "No One You Know",
    "SongTitle": "Call Me Today",
    "AlbumTitle": "Somewhat Famous",
    "Year": 2015,
    "Price": 2.14,
    "Genre": "Country",
    "Tags": {
        "Composers": [
            "Smith",
            "Jones",
            "Davis"
        ],
        "LengthInSeconds": 214
    }
}
# r = conn.put_item(
#     table_name='Music',
#     item=item
# )
# print r
print '????????????????????????????????????????????????????????????????????????????????'


print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
# Delete table
description = conn.delete_table('Music')
print description
# {
#   u'TableDescription': {
#     u'TableArn': u'arn:aws:dynamodb:ddblocal:000000000000:table/Music',
#     u'AttributeDefinitions': [
#       {
#         u'AttributeName': u'Artist',
#         u'AttributeType': u'S'
#       },
#       {
#         u'AttributeName': u'SongTitle',
#         u'AttributeType': u'S'
#       }
#     ],
#     u'ProvisionedThroughput': {
#       u'NumberOfDecreasesToday': 0,
#       u'WriteCapacityUnits': 1,
#       u'LastIncreaseDateTime': 0.0,
#       u'ReadCapacityUnits': 1,
#       u'LastDecreaseDateTime': 0.0
#     },
#     u'TableSizeBytes': 0,
#     u'TableName': u'Music',
#     u'TableStatus': u'ACTIVE',
#     u'KeySchema': [
#       {
#         u'KeyType': u'HASH',
#         u'AttributeName': u'Artist'
#       },
#       {
#         u'KeyType': u'RANGE',
#         u'AttributeName': u'SongTitle'
#       }
#     ],
#     u'ItemCount': 0,
#     u'CreationDateTime': 1486632404.093
#   }
# }
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

