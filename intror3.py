#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(1)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.queue_declare(queue='hello')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
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