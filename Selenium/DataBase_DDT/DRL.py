import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", port=3307, user="root",
                                         passwd="root", database="mydb")
    cur = connection.cursor()
    cur.execute("SELECT * FROM student;")
    print(type(cur))
    for row in cur:
        print(row[0], row[1], row[2])
    # no need to con.commit() as we are fetching data from sql
    cur.close()
except:
    print("Connection to Sql database Failed")
print("Finished...")