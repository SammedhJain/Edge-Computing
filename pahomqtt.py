from array import array
import paho.mqtt.client as mqtt  #import the client1
import time
import os
payloads=[]

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    payloads.append(msg.payload)
    print(msg.topic + " " + str(msg.payload))



def pub_del(topic,clients):       

    mqtt.Client.connected_flag=False#create flag in class
    broker="192.168.1.6"
    client = mqtt.Client("python1")             #create new instance 
    client.on_connect=on_connect  #bind call back function
    client.loop_start()
    print("Connecting to broker ",broker)
    client.connect(broker)      #connect to broker
    while not client.connected_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    print("in Main Loop")

    client.loop_stop()    #Stop loop 
    #client.disconnect() # disconnect
    #array =['aaaa','bbb']
    #topic ='device_management/delete'
    for i in clients:
        client.publish(topic, i)

  

