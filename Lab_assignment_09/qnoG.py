import sqlite3

# Connect to the database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Specify the employee ID to delete
emp_id = 3  # Change this to the desired employee ID

# Delete query
cursor.execute("DELETE FROM Employee WHERE id = ?", (emp_id,))
conn.commit()

# Fetch and display the remaining records
cursor.execute("SELECT * FROM Employee")
remaining_employees = cursor.fetchall()

print("Remaining Employees after deletion:")
for emp in remaining_employees:
    print(emp)

conn.close()
