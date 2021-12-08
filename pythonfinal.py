import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "YU_oppdivide!20",
  database= "menagerie"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE pet")

for x in mycursor:
  print(x) 
