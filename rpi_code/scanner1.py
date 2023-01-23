from scapy.all import ARP, Ether, srp
import mysql.connector
import time
from test1 import *
#from datamodified import *
#from deletedb import*
import os
while True:
    target_ip = "192.168.1.13/24"

    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []

    for sent, received in result:
        clients.append(received.psrc)

        
            
    database(clients)
    

        
    




    