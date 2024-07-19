import pika
import time
import random 
import csv

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))
channel = connection.channel()
counter = 0
start_time = time.time()
channel.queue_declare(queue='hello.error')
troughput = []
def callback(ch, method, properties, body):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    if elapsed_time > 300:

        with open('pontos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['X', 'Y'])  # Cabeçalho opcional
            writer.writerows(troughput)
            exit()
    #print(f" [x] Received {body.decode()}")
    message = body
    global counter 
    P = random.randint(1, 4)
    if P != 1:
        channel.basic_publish(exchange='',
                            routing_key='hello.error',
                            body=message)
    else:
        channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=message)
        end_time = time.time()
        elapsed_time = end_time - start_time
        counter = counter + 1 
        point = [counter/elapsed_time, elapsed_time]
        troughput.append(point)

    #print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello',
                      on_message_callback=callback)

#print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
end_time = time.time()
elapsed_time = end_time - start_time 



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)