import mysql.connector

connection = mysql.connector.connect(host="localhost", port="3307", user="root",
                                     passwd="root", database="mydb")

insert_query = "INSERT INTO student VALUES(106, 'Sakshi', 45)"
update_query = "UPDATE student SET marks = 90 WHERE SNO = 103"
delete_query = "DELETE FROM student WHERE SNO = 105"

cursor = connection.cursor()
# cursor.execute(insert_query)
# cursor.execute(update_query)
cursor.execute(delete_query)
connection.commit()
connection.close()
