#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
    )
channel = connection.channel()  #声明管道

#声明queue
channel.queue_declare(queue="hello1",durable=True)#duranble:队列持久化,服务宕机队列无影响

#RabbitMQ
channel.basic_publish(exchange='',
                      routing_key='hello1',
                      body='Hello World!',
                      properties=pika.BasicProperties( #负责消息持久化
                          delivery_mode=2,
                      ))
print("[x] Sent 'Hello World!'")
connection.close()