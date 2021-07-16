#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "info:Hello World!" #手动输入消息，没有发送hello world
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print("[x] Sent %r" % message)

connection.close()