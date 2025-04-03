import sqlite3

# Connect to the database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Query to get the average salary per department
cursor.execute("SELECT department, AVG(salary) FROM Employee GROUP BY department")
avg_salaries = cursor.fetchall()

print("Average salary per department:")
for dept, avg_salary in avg_salaries:
    print(f"Department: {dept}, Average Salary: {avg_salary}")

conn.close()
