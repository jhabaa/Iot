"""mqtt.py
Code de connection au Brocker MQTT.
"""
import paho.mqtt.client as mqtt
import time

import math
import json




message = {}
textTopic = "Groupe10"
#messagesFromBrokerLabel = StringVar()
def on_connect(client, userdata, flags, rc): #Code lancé à la connexion au broker
   if rc==0:
        client.connected_flag = True #Set flag #Le Flag nous permet d'exécuter une action spécifique si la connection est active ou pas
        print("connected ok")
        client.subscribe(textTopic) #Souscription au Topic 
   else:
       print("Bad connection")

def on_message(client, userdata, msg): #Code exécuté à la reception d'un messge
    #print (f"received '{str(msg.payload)} from '{msg.topic}'")
    alist = str(msg.payload.decode("utf-8", "ignore"))
    #print ("Data receive type", type(alist))
    #print("Data receive", alist)
    #recover = json.loads(alist) #Decode json data
    #print (recover[1][1])
    print (alist)
    #messagesFromBrokerLabel.set(messagesFromBrokerLabel.get() + str(msg.payload) +" FROM" + msg.topic +"\n") 
    

def startMQTTConnection(): #Ce code est celui de la connexion au broker de l'ISIB 
    mqtt.Client.connected_flag = False #Create flag in class
    client = mqtt.Client("hean")#Nouvelle instance avec un nom. Il ne doit juste pas être le même que l'émetteur 
    client.username_pw_set(username="guest", password="guest") 
    client.on_connect=on_connect  #bind call back function
    client.on_message = on_message #Exécute la fonction on_message pour chaque message reçu
    print("Connecting to broker", "172.30.4.52") 
    client.connect("90.90.0.3")  #connect to broker
    #time.sleep(10)
    #client.loop_forever()
      
        
startMQTTConnection()



