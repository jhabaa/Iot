#!/usr/bin/env python
import pika
import sys
import asyncio
import socketio
from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage
import json

#Async connection to RabbitMQ to retrieve datas
"""
async def on_message(message: AbstractIncomingMessage) -> None:
    #Cette fonction nest pas necessairement définie comme asynchrone; Mais cest possible: regarde
    print(message.body)
    await asyncio.sleep(5) #async I/O operations
"""   
""" 
async def rabbit()-> None:
    #Etablissement de la connection
    connection = await connect("amqp://guest:guest@90.90.0.3/")
    async with connection:
        #Creation d'une chaine
        channel = await connection.channel()
        #Declaration de notre chaine comme topic
        exchange = await channel.declare_exchange(name='isib',type='topic')
        queue = await channel.declare_queue('', exclusive=True)
        #queue_name = await result.method.queue
        await queue.bind(
            exchange='isib',routing_key='isib'
        )
        #On ecoute sur le topic 
        #await exchange.publish(, routing_key='isib')
        print(" [*] Waiting for messages. To exit press CTRL+C")
        await channel.get_exchange(name='isib')
        
        await asyncio.Future()
"""
"""


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='90.90.0.3'))
channel = connection.channel()

channel.exchange_declare(exchange='isib', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='isib', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

"""
sio = socketio.AsyncClient()
async def connectMe():
    
    @sio.event
    async def connect():
        print('connection established')
        await sio.emit('my response', {'response': 'my response'})
    """
    @sio.event
            
    async def my_message(data):
        print('message received with ', data)
        await sio.emit('my response', {'response': 'my response'})
    """       
    @sio.event
    async def disconnect():
        print('disconnected from server')

    
    await sio.connect('http://localhost:8080')
    await sio.emit("my message","I can send a message")
    print("Start communication")
    await (rabbit3()) 
    #await sio.wait()
    
    #asyncio.run(ConnectToSocket())
    #asyncio.run(sendData())


#asyncio.run(rabbit())

async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        
        print(type(json.loads(message.body.decode())))
        await sio.emit("my message",message.body.decode())

        
       

async def rabbit3() -> None:
    # Perform connection
    connection = await connect("amqp://hean:hean@heanlab.com/")
    
    async with connection:
        # Creating a channel
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        logs_exchange = await channel.declare_exchange(
            "isib", ExchangeType.TOPIC,
        )

        # Declaring queue
        queue = await channel.declare_queue(exclusive=True)

        # Binding the queue to the exchange
        await queue.bind(logs_exchange,routing_key='isib')
        
        # Start listening the queue
        await queue.consume(on_message)

        print(" [*] Waiting for logs. To exit press CTRL+C")
        await asyncio.Future()
        


asyncio.run(connectMe())





