import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

cursor.execute("SELECT department, AVG(salary) FROM Employees GROUP BY department")
avg_salaries = cursor.fetchall()

print("Average salary per department:")
for dept, avg_salary in avg_salaries:
    print(f"Department: {dept}, Average Salary: {avg_salary}")

conn.close()
