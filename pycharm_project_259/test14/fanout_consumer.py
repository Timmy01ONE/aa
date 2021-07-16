#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
restult = channel.queue_declare('',exclusive=True)
#exclusive排他，唯一的，不指定queue名字，rabbit会随机分配一个名字。
# exclusive-True会在使用此queye的消费者断开后，自动将queue删除

queue_name = restult.method.queue
print("random queuename",queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      )#no_ack=True
channel.start_consuming()