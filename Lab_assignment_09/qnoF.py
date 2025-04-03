import sqlite3

# Connect to the database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Specify the employee ID to update
emp_id = 2  # Change this to the desired employee ID

# Update query
cursor.execute("UPDATE Employee SET salary = salary * 1.10 WHERE id = ?", (emp_id,))
conn.commit()

# Fetch and display the updated record
cursor.execute("SELECT * FROM Employee WHERE id = ?", (emp_id,))
updated_emp = cursor.fetchone()
print("Updated Employee Record:", updated_emp)

conn.close()
