import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Employees")
fetch_employee = cursor.fetchall()
for data in fetch_employee:
    print(data)

conn.close()
