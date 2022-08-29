"""mqtt.py
Code de connection au Brocker MQTT.
"""
import paho.mqtt.client as mqtt
import time
from tkinter import *
from tkinter import ttk
import asyncio
import math
import json

"""
root = Tk()
root.title("MQTT APP - Groupe 10")
root.geometry("400x500")
mainframe = ttk.Frame(root)
mainframe.pack()


messagesFromBroker = ["test", "testEncore", "retour"]"""
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
    print (f"received '{str(msg.payload)} from '{msg.topic}'")
    #messagesFromBrokerLabel.set(messagesFromBrokerLabel.get() + str(msg.payload) +" FROM" + msg.topic +"\n") 
    print("Ok")
    

def changeText():
    messagesFromBrokerLabel.set(messagesFromBroker)

def startMQTTConnection(): #Ce code est celui de la connexion au broker de l'ISIB 
    mqtt.Client.connected_flag = False #Create flag in class
    client = mqtt.Client("ReceiverFromTopic")#Nouvelle instance avec un nom. Il ne doit juste pas être le même que l'émetteur 
    client.username_pw_set(username="isib", password="oups_pas_de_lora") 
    client.on_connect=on_connect  #bind call back function
    client.on_message = on_message #Exécute la fonction on_message pour chaque message reçu
    print("Connecting to broker", "172.30.4.52") 
    client.connect("172.30.4.52")  #connect to broker
    time.sleep(10) # attendre que la connexion s'effectue
    client.loop_forever()#Stop loop 
      
        
startMQTTConnection()
