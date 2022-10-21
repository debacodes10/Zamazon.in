import mysql.connector
from mysql.connector import Error
try:
     conn = mysql.connector.connect(host='hostname',
                         database='db',
                         user='root',
                         password='')
     if conn.is_connected():
       cursor = conn.cursor()
       cursor.execute("select database();")
       record = cursor.fetchall()
       print ("You're connected to - ", record)
except Error as e :
    print ("Print your error msg", e)
finally:
    #closing database connection.
    if(conn.is_connected()):
        cursor.close()
        conn.close()