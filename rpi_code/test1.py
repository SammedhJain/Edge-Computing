import mysql.connector
#clients=['1','apple','2022','101','ygvsvg','192.268.66.2']
from deletedb import *
from insertdb import *
from pahomqtt import *
#from mqtt_client import *


def database(clients):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="mysql@123",
      database="ipaddress"
    )

    mycursor = mydb.cursor(buffered=True)
        #query1 = "SELECT ipaddr FROM ip_addr WHERE ipaddr NOT IN(SELECT ipaddr FROM ip_addr WHERE ipaddr in (clients))"
    query1 = "SELECT * FROM ip_addr"
    mycursor.execute(query1)
    a=[]
    for i in mycursor:
        a.append(i)
    b=[] # ip present in database
    for i in range(0,len(a)):
        x= a[i][1]
        b.append(x)
    delete1 =[]
    for item in b:
        if(item not in clients):
            delete1.append(item)
    print(delete1)
    delete(delete1)
    insert1 =[]
    for item in clients:
        if(item not in b):
            insert1.append(item)
    print("insert")
    print(insert1)
    insert(insert1)
   
    
    
    
    
    
    mydb.commit()
    


#database(clients)