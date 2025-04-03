import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

# Query to get total employees and maximum salary
cursor.execute("SELECT COUNT(*) AS total_employees, MAX(salary) AS max_salary FROM Employees")
result = cursor.fetchone()

# Display results
print(f"Total number of employees: {result[0]}")
print(f"Maximum salary: {result[1]}")

# Close the connection
conn.close()
