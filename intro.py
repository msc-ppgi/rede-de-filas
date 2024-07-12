import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(0,20):
    message = ' '.join(sys.argv[1:]) if sys.argv[1:] else f"Hello World! -> {i}"
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print(f" [x] Sent {message}")

connection.close()

