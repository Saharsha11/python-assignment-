import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

emp_id = 3  # Change this to the employee ID you want to delete

cursor.execute("DELETE FROM Employees WHERE id = %s", (emp_id,))
conn.commit()

cursor.execute("SELECT * FROM Employees")
remaining_employees = cursor.fetchall()

print("Remaining Employees after deletion:")
for emp in remaining_employees:
    print(emp)

conn.close()
