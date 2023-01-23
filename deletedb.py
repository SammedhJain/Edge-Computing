import mysql.connector
from insertdb import *
from pahomqtt import *

def delete(a):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123",
        database="ipaddress"
        )
        mycursor =mydb.cursor()
        for i in a:
            query2 = "DELETE FROM ip_addr WHERE ipaddr = %s "
            mycursor.execute(query2,(i,))
        mydb.commit()
        topic ='delete'
        pub_del(topic,a)






        

