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
[订阅端]
需要声明 exchange
需要声明 queue
需要将 exchange 和 queue 绑定

订阅段从 queue 中订阅 message
"""

ed = channel.exchange_declare(
    exchange='logs',
    type='fanout',
)
print ed  # <METHOD(['channel_number=1', 'frame_type=1', 'method=<Exchange.DeclareOk>'])>

qd = channel.queue_declare(
    queue='',
    durable=True,  # make the queue durable (survive reboots of the broker)
    exclusive=True,  # once we disconnect the consumer the queue should be deleted
)
print qd  # <METHOD(['channel_number=1', 'frame_type=1', "method=<Queue.DeclareOk(['consumer_count=0', 'message_count=0', 'queue=amq.gen-gJjOuCm8OapkpK2wifwbHy'])>"])>
queue_name = qd.method.queue
print queue_name  # amq.gen-gJjOuCm8OapkpK2wifwbHy

qb = channel.queue_bind(
    exchange='logs',
    queue=queue_name,
)
print qb  # <METHOD(['channel_number=1', 'frame_type=1', 'method=<Queue.BindOk>'])>
print '----------------------------------------------------------------------------------------------------'

def callback(ch, method, properties, body):
    print('[x] Received: %s' % body)

bc = channel.basic_consume(
    consumer_callback=callback,
    queue=queue_name,
    no_ack=True,
)
print type(bc)  # <type 'str'>
print bc  # ctag1.143b3cc34e804d2885231e86b34b5be5

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
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
