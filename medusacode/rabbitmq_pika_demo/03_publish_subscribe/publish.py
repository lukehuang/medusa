#!/usr/bin/env python
# coding:utf-8

import pika
import datetime

HOST = '192.168.100.100'
PORT = 5672
QUEUE_NAME = 'log_queue'

print '----------------------------------------------------------------------------------------------------'
connection = pika.BlockingConnection(
    parameters=pika.ConnectionParameters(
        host=HOST,
        port=PORT,
    )
)
print connection  # <pika.adapters.blocking_connection.BlockingConnection object at 0x109564b50>

channel = connection.channel(
    channel_number=None
)
print channel  # <pika.adapters.blocking_connection.BlockingChannel object at 0x1098355d0>
print '----------------------------------------------------------------------------------------------------'

"""
[发布端]

只需要声明 exchange
不需要声明 queue
不需要将 exchange 和 queue 绑定

发布端把 message 发布到 exchange
"""

ed = channel.exchange_declare(
    exchange='logs',
    type='fanout',
)
print ed  # <METHOD(['channel_number=1', 'frame_type=1', 'method=<Exchange.DeclareOk>'])>

print '----------------------------------------------------------------------------------------------------'

message = datetime.datetime.now()
message = str(message)

bp = channel.basic_publish(
    exchange='logs',  # the exchange name
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    )
)
print bp  # True
print '[x] Sent: %s' % message

connection.close()
print '----------------------------------------------------------------------------------------------------'

"""
The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue.
Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.
Instead, the producer can only send messages to an exchange.

An exchange is a very simple thing.
On one side it receives messages from producers
and on the other side it pushes them to queues.

The exchange must know exactly what to do with a message it receives.
Should it be appended to a particular queue?
Should it be appended to many queues?
Or should it get discarded?

The rules for that are defined by the exchange types: direct, topic, headers, fanout.

The relationship between exchange and a queue is called a binding.
"""
