#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout') #exchange_type='topic'表示搜索批量的内容，“#”表示收所有
restult = channel.queue_declare('',exclusive=True)
queue_name = restult.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
print(severities)
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)  #识别名为severity的内容接收
print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] %r:%r" % (method.routing_key, body))

channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      ) #no_ack=True
channel.start_consuming()