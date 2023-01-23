import mysql.connector
from pahomqtt import *
def insert(clients):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@123",
    database="ipaddress"
    )
    mycursor =mydb.cursor()
    for i in clients:
        # print(i)
        sql = "INSERT INTO ip_addr(ipaddr) VALUES(%s)"
        mycursor.execute(sql,(i,))
            

    topic ='insert'
    pub_del(topic,clients)       
    mydb.commit()
