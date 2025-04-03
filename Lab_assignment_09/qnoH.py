import sqlite3

conn = sqlite3.connect('sql.db')

cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * from Employee")
employees = cursor_obj.fetchall()
print("Total number of employees =", len(employees))

cursor_obj.execute("SELECT * FROM Employee WHERE salary = (SELECT MAX(salary) FROM Employee)")
maximum_salary = cursor_obj.fetchall()

print("Employee(s) with the highest salary:")
for employee in maximum_salary:
    print(employee)

conn.close()