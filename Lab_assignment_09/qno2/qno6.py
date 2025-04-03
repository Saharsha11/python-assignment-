import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

emp_id = 2  # Change this to the employee ID you want to update

cursor.execute("UPDATE Employees SET salary = salary * 1.10 WHERE id = %s", (emp_id,))
conn.commit()

cursor.execute("SELECT * FROM Employees WHERE id = %s", (emp_id,))
updated_emp = cursor.fetchone()

print("Updated Employee Record:", updated_emp)

conn.close()
