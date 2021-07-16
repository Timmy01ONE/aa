#!/usr/bin/env python
import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello1',durable=True)#duranble:队列持久化,服务宕机队列无影响

def callback(ch, method, properties, body):
    print("-->",ch,method,properties)
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1) #设置权重
channel.basic_consume( #开始消费消息
                        queue='hello1',
                        on_message_callback=callback,
                        auto_ack=False) #auto_ack表示默认不进行高可用

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()