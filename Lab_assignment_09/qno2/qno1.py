import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

# Create Employees table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        department VARCHAR(255),
        salary FLOAT,
        hire_date DATE
    )
""")

print("Employees table created successfully.")

conn.close()
