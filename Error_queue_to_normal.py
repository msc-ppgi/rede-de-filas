#!/usr/bin/env python
import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))
channel = connection.channel()


channel.queue_declare(queue='hello.error')

def callback(ch, method, properties, body):
    #print(f" [x] Received {body.decode()}")
    message = body
    #time.sleep(1)
    P = random.randint(1, 4)
    if P != 1:
        channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=message)
    else:
        channel.basic_publish(exchange='',
                    routing_key='hello.error',
                    body=message)
    #print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello.error',
                      on_message_callback=callback)

#print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)