import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM flights where fcode=103")
myresult = mycursor.fetchall()
print(myresult[0][0])
'''for x in myresult:
  print(x)

print(mydb)'''