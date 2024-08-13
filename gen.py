import pika
import os 
import threading
import random 
import time
import matplotlib.pyplot as plt
import csv

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))

global channel, channelNE
channel = connection.channel()


class GoToMainException(Exception):
    pass

def NormalToError():
    try:
        global channelNE
        channelNE = ""
        if channelNE is open:
            print("fechou a conexão")
            channelNE.close()
        connectionNE = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.35'))
        channelNE = connectionNE.channel()
        print("retorno normaltoerro ", retorno)
        global counter
        counter = 0
        global start_time 
        start_time = time.time()
        global troughput
        troughput = []

        #while retorno == 0:  
        channelNE.basic_qos(prefetch_count=1)
        
        channelNE.basic_consume(queue='hello',
                            on_message_callback=callbackNE)

        channelNE.start_consuming()
    except GoToMainException:
        return

def callbackNE(ch, method, properties, body):
    global counter
    global retorno
    global troughput
    global a
    end_time = time.time()
    elapsed_time = end_time - start_time

    if int(elapsed_time) % 10 == 0 and int(elapsed_time) != a:
        print(a)
        a = int(elapsed_time)

        
    if value > 10000:
        print("dentro da tentativa de retorno")
        try:
            principal(False)
        except GoToMainException:
            raise GoToMainException
    path = str(value) + "/pontos.csv"
    if elapsed_time > 300 and value <= 10000:

        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['X', 'Y'])  # Cabeçalho opcional
            writer.writerows(troughput)
        plot()
        retorno = 1
        print("retorno dentro ", retorno)
        principal(False)
    #print(f" [x] Received {body.decode()}")
    message = body
    P = random.randint(1, 4)
 
    if P != 1:
        channelNE.basic_publish(exchange='',
                            routing_key='hello.error',
                            body=message)
    else:
        channelNE.basic_publish(exchange='',
                    routing_key='hello',
                    body=message)
        end_time = time.time()
        elapsed_time = end_time - start_time
        counter = counter + 1 
        point = [counter/elapsed_time, elapsed_time]
        troughput.append(point)

    #print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

def ErroToNormal():
    while True:
        channel.basic_qos(prefetch_count=1)

        channel.basic_consume(queue='hello.error',
                        on_message_callback=callbackEN)
        channel.start_consuming()
    
def callbackEN(ch, method, properties, body):
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

def plot():
    print("Plot")
    x = []
    y = []
    title = "Troughput de N = " + str(value)
    pathg  = str(value) + "/Figure_1.png"
    path  = str(value) + "/pontos.csv"
    with open(path, 'r') as file:
        print("path - > ", path, " file -> ", file)
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            x.append(float(row[0]))  # Converter para float
            y.append(float(row[1]))  # Converter para float

    # Plotando os pontos
    plt.plot(y, x, 'o-')  # 'o-' para pontos conectados por linhas
    plt.xlabel('t')
    plt.ylabel('troughput')
    plt.title(title)
    plt.savefig(pathg)  # Pode ser .png, .jpg, .pdf, .svg, etc.
    plt.close()


global retorno
retorno = 0
global counter 
counter = 0
global value 
value = 1000
value_old = 0
increment = 1000
global elapsed_time
global troughput
global a 
a = 0

def principal(first):
    global value, increment, connectionNE, channelNE, retorno
    print("value dentro do principal, ", value)
    if first == False:
        channelNE.close()
        retorno = 0 
    if value > 10000:
        raise GoToMainException
    while value <= 10000:
        if not os.path.exists(str(value)):
            os.makedirs(str(value))
            for i in range(0,value):
                message = f"Hello World! -> {i}"
                print(message)
                channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=message)
            elapsed_time = 0
            NormalToError()      
            
        channel.queue_purge("hello")
        value = value + increment
        if value > increment * 10:
            increment = increment * 10
    


principal(True)
connection.close()
