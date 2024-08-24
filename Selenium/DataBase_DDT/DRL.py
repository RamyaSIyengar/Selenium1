import mysql.connector

connection = mysql.connector.connect(host="localhost", port=3307, user="root",
                                     passwd="root", database="mydb")
cur = connection.cursor()
cur.execute("SELECT * FROM student;")
for row in cur:
    print(row[0], row[1], row[2])