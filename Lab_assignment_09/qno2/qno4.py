import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Employees WHERE salary > 50000 ORDER BY hire_date DESC")
filtered_employees = cursor.fetchall()

print("Employees with salary > 50,000 sorted by hire_date:")
for emp in filtered_employees:
    print(emp)

conn.close()
