import sqlite3

# Connect to the database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Query to filter employees
cursor.execute("SELECT * FROM Employee WHERE salary > 50000 ORDER BY hire_date DESC")
filtered_employees = cursor.fetchall()

print("Employees with salary greater than 50,000 sorted by hire_date (descending):")
for emp in filtered_employees:
    print(emp)

conn.close()


