import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_assignment"
)
cursor = conn.cursor()

# Insert multiple employee records
employees = [
    ("Alice", "HR", 60000, "2022-05-15"),
    ("Bob", "IT", 75000, "2021-03-10"),
    ("Charlie", "Finance", 55000, "2020-07-22"),
    ("David", "IT", 90000, "2019-11-30"),
    ("Eve", "Marketing", 48000, "2023-01-05"),
]

cursor.executemany("INSERT INTO Employees (name, department, salary, hire_date) VALUES (%s, %s, %s, %s)", employees)
conn.commit()

print("Sample employee data inserted successfully.")



conn.close()
